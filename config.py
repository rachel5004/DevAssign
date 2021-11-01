import os
import secrets
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'urlcutter.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY=secrets.token_hex(16)