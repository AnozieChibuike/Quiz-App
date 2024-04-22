from app import db
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")

class Quiz(BaseModel):
    
    """
        Quiz Model Mapped to a Table
    """
    title: Mapped[str] = db.Column(db.String(100), nullable=False)
    category_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('category.id'), nullable=False)
    questions = db.relationship('Question', backref='quiz', lazy=True)

    
    def __repr__(self):
        return f"<Quiz {self.id}>"
