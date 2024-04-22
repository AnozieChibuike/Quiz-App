from app import db
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")

class Option(BaseModel):
    
    """
        Option Model Mapped to a Table
        This is Question options
    """
    text: Mapped[str] = db.Column(db.String(255), nullable=False)
    is_correct: Mapped[bool] = db.Column(db.Boolean, default=False, nullable=False)
    question_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('question.id'), nullable=False)
    
    def __repr__(self):
        return f"<Option {self.id}>"
