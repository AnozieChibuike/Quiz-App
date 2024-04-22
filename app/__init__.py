from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # type: ignore[import-untyped]
from config import Config


app: Flask = Flask(__name__)
app.config.from_object(Config)

db: SQLAlchemy = SQLAlchemy(app)
migrate: Migrate = Migrate(app, db)

from  app import routes
from app import models