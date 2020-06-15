# pythonの最新版をベースに使用
FROM python:latest

# 作業ディレクトリ作成
WORKDIR /workdir

# pipをアップグレード
RUN pip install --upgrade pip && pip install \
    bootstrap4 \
    Django \
    djangorestframework \
    djangorestframework-jwt \
    django-extensions \
    django-bootstrap4

# ポート
EXPOSE 8000

# webサーバー起動
ENTRYPOINT [ "python", "manage.py", "runserver"]

# 必要に応じてrunコマンド実行時に書き換え
CMD ["0.0.0.0:8000"]
