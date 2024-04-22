from app import db
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")

class Category(BaseModel):
    
    """
        Category Model Mapped to a Table
        This is quiz Category
    """
    name: Mapped[str] = db.Column(db.String(100), nullable=False)
    quizzes = db.relationship('Quiz', backref='category', lazy=True)
    
    def __repr__(self):
        return f"<Category {self.name}>"
