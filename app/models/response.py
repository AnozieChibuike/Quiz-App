from app import db
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")

class Response(BaseModel):    
    """
        Response Model Mapped to a Table
        This is user response to a question
    """
    attempt_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('attempt.id'), nullable=False)
    question_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('question.id'), nullable=False)
    option_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('option.id'), nullable=False)

    def __repr__(self):
        return f"<Response {self.id}>"
