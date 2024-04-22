from app import db
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")

class Question(BaseModel):
    
    """
        Question Model Mapped to a Table
        This is quiz Questions
    """
    text: Mapped[str] = db.Column(db.String(255), nullable=False)
    quiz_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('quiz.id'), nullable=False)
    options = db.relationship('Option', backref='question', lazy=True)

    
    def __repr__(self):
        return f"<Question {self.id}>"
