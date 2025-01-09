import os

class Config:
    USER= os.environ.get('POSTGRES_USER', 'superdude')
    PASSWORD= os.environ.get('POSTGRES_PASSWORD', '102010')
    HOST= os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT= os.environ.get('POSTGRES_PORT', 5432)
    DB= os.environ.get('POSTGRES_DB', 'funkydb')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'wn1a3fncz2ayhapg2o1xznmuf'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'salim.nogorbekov@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'jamesfox23')