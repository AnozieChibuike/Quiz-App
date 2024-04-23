from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # type: ignore[import-untyped]
from config import Config
from flask_jwt_extended import JWTManager
from flask_mail import Mail # type: ignore[import-untyped]
from flask_cors import CORS

app: Flask = Flask(__name__)
app.config.from_object(Config)

db: SQLAlchemy = SQLAlchemy(app)
migrate: Migrate = Migrate(app, db)
jwt = JWTManager(app) 
mail = Mail(app)


CORS(app)


from  app import routes
from app import models