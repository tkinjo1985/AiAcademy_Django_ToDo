import environ
from .base import *


# .envからSECRET_KEYを読み込む
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

# 開発時はデバッグをTrueにする
DEBUG = True

# 全てのホストからのアクセスを許可
ALLOWED_HOSTS = ['*', 'testserver']

# .envからDatabaseを読み込む
DATABASES = {
    'default': env.db()
}
