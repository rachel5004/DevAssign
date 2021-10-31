import os
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DB_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'urlcutter.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False