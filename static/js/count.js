$(function () {

    var initial_text_length = 0; // 初期値
    // var text_max_length = JSON.parse(document.getElementById('text_max_length').textContent);

    $(".count").text(initial_text_length - $("#id_content").val().length);

    $("#id_content").on("keydown keyup keypress change", function () {
        var text_length = $(this).val().length;
        $(".count").text(text_length); // 入力文字数
        // $(".count_1").text(countdown);
    });
});
