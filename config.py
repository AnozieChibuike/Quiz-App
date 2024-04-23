# Flask Configurations

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.getenv('EMAIL_SERVER_HOST','smtp.gmail.com')
    MAIL_PORT=465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME=os.getenv('EMAIL_SERVER_USER')
    MAIL_PASSWORD=os.getenv('EMAIL_SERVER_PASSWORD')
    MAIL_DEFAULT_SENDER=os.getenv('EMAIL_FROM')
    MAIL_DEFAULT_SENDER_NAME=os.getenv('EMAIL_NAME')
    ORIGIN = 'http://localhost:5173'