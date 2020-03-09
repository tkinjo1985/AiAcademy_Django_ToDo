window.onload = function () {
    const onKeyDown = function (ev) {
        if (((ev.keyCode != 9) && (ev.keyCode != 32)) || ev.ctrlKey || ev.altKey) { return true; }
        ev.preventDefault();
        const str = (ev.keyCode == 32) ? " " : "\t", TABWIDTH = 4, CRLF = [13, 10];
        let e = ev.target, start = e.selectionStart, end = e.selectionEnd, sContents = e.value, top = e.scrollTop;
        if ((start == end) || !sContents.includes("\n")) {
            e.setRangeText(str, start, end, "end");
            return;
        }
        if (CRLF.indexOf(sContents.charCodeAt(end - 1)) < 0) {
            for (; end < sContents.length; end++) {
                if (CRLF.indexOf(sContents.charCodeAt(end)) >= 0) { break; }
            }
        }
        for (; start > 0; start--) {
            if (CRLF.indexOf(sContents.charCodeAt(start - 1)) >= 0) { break; }
        }
        let v = sContents.substring(start, end).split("\n");
        for (let i = 0; i < v.length; i++) {
            if (v[i] == "") { continue; }
            if (!ev.shiftKey) {     //indent
                v[i] = str + v[i];
            } else {                //unindent
                if (str == "\t") {
                    for (let j = 0, c = " "; (j < TABWIDTH) && (c == " "); j++) {
                        c = v[i].substring(0, 1);
                        if ((c == " ") || (j == 0 && c == "\t")) { v[i] = v[i].substring(1); }
                    }
                } else if (v[i].substring(0, 1) == " ") {
                    v[i] = v[i].substring(1);
                }
            }
        }
        e.setRangeText(v.join("\n"), start, end, "select");
    }

    document.getElementById("id_content").addEventListener("keydown", onKeyDown);
}
