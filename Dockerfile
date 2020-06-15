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

CMD ["/bin/bash"]
