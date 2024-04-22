from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")


class User(BaseModel):
    
    """
        User Model Mapped to a Table
    """
    
    fullname: Mapped[str] = db.Column(db.String(50), nullable=False)
    email: Mapped[str] = db.Column(db.String(120), index=True, unique=True)
    username: Mapped[str] = db.Column(db.String(120), index=True, unique=True)
    bio: Mapped[str] = db.Column(db.String(500), default="")
    phone: Mapped[str] = db.Column(db.String(11), nullable=False, unique=True)
    password_hash: Mapped[str] = db.Column(db.String(1024))
    image_url: Mapped[str] = db.Column(db.String(500))
    email_verified: Mapped[bool] = db.Column(db.Boolean, default=False)
    is_admin: Mapped[bool] = db.Column(db.Boolean, default=False)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")
        
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.email}>"
