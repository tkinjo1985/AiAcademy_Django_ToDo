# pythonの最新版をベースに使用
FROM python:latest

# 作業ディレクトリ作成
WORKDIR /workdir

# pipをアップグレード
RUN pip install --upgrade pip

COPY requirements.txt /workdir
RUN pip install -r requirements.txt

# ポート
EXPOSE 8000

CMD ["/bin/bash"]
