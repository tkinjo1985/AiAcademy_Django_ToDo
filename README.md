# AiAcademy_Django_ToDo
AiAcademyの「FlaskとMySQLでToDoアプリを実装しよう」をDjangoとSQLite3で実装

### バックエンド
- Webフレームワーク: Django
- DB: SQLite3 
- REST API: rest_framework

### フロントエンド
- Template: Django HTML、Django-Bootstrap4

### 使い方
$ git clone https://github.com/tkinjo1985/AiAcademy_Django_ToDo.git
$ cd AiAcademy_Django_ToDo
$ python manager.py makemigrations
$ python manager.py migrate
$ python manager.py runserver

### REST APIの仕様
POST: api/token/ 認証用トークンの取得(username, password)

GET: api/entries/ ユーザーに紐付いたToDoを取得
GET: api/entries/<todo_id> todo_id指定でtodo単体取得

POST: api/entries/ 新規ToDoの作成(name, content, user)
