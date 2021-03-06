# AiAcademy_Django_ToDo
AiAcademyの「FlaskとMySQLでToDoアプリを実装しよう」をDjangoとSQLite3で実装

### バックエンド
- Webフレームワーク: Django(Dcokerコンテナを使用)
- DB: SQLite3 
- REST API: rest_framework

### フロントエンド
- Template: DjangoHTML、Django-Bootstrap4

### 使い方
```
# リポジトリをクローン
$ git clone https://github.com/tkinjo1985/AiAcademy_Django_ToDo.git
$ cd AiAcademy_Django_ToDo

# docker-composeでコンテナを起動
$ docker-compose up --build -d
```

### REST APIの使用方法
- POST: api/token/ 認証用トークンの取得
```
# pythonとrequestsを用いた認証トークンの取得

import requests

# トークン取得用URL
url = 'http://127.0.0.1:8000/api/token/'

user = {
    'username': <username>,
    'password': <password>
    }
res = requests.post(url, data=user)
print(res.text)
----
'{"token":"eyJ0eXA...."}'
----

```

- POST: api/entries/ 新規ToDoの作成(name, content, user)
```
# pythonとrequestsを用いた新規ToDoの作成

import requests

# 新規ToDoの作成用URL
url = 'http://127.0.0.1:8000/api/entries/'

# 追加するToDoの情報
todo = {
    'name': 'test_todo',
    'content': 'test_todo_content',
    'user': 1
}

# 取得したトークンをヘッダーに追加
header = {
    'Authorization': 'JWT '+ <取得したtoken>
}

todo = requests.post(url, headers=header, data=todo)
```

- GET: api/entries/ ユーザーに紐付いたToDoを取得
- GET: api/entries/<todo_id> todo_id指定でtodo単体取得
```
# pythonとrequestsを用いたToDoの取得

import requests

# todo取得用URL
# 特定のtodoだけを取得する場合は'api/entries/<todo_id>'
url = 'http://127.0.0.1:8000/api/entries/'


header = {
    'Authorization': 'JWT '+ <取得したtoken>
}

todo = requests.get(url, headers=header)
```
