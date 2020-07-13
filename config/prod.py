import environ
import dj_database_url
from .base import *

# 本番環境ではデバックをFalse
DEBUG = False

# Herokuに設定した環境変数から読み込む
env = environ.Env()
SECRET_KEY = env('SECRET_KEY')

# Herokuドメインからのアクセスのみ許可
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# HerokuのPostgresへ接続
db_from_env = dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config()
}
