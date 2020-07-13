# pythonの最新版をベースに使用
FROM python:latest

# 作業ディレクトリ作成
WORKDIR /workdir

RUN apt-get update && apt-get install -y sudo

# pipをアップグレード
RUN pip install --upgrade pip

COPY requirements.txt /workdir
RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
