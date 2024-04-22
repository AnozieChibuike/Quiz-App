from app import db
from app.models.base import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped

load_dotenv()

base_url = os.getenv("BASE_URL")

class Attempt(BaseModel):
    
    """
        Attempt Model Mapped to a Table
        This is quiz attempts of a user
    """
    quiz_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('quiz.id'), nullable=False)
    user_id: Mapped[str] = db.Column(db.String(126), db.ForeignKey('user.id'), nullable=False)
    score: Mapped[int] = db.Column(db.Integer, default=0)  # Store the score as an integer
    responses = db.relationship('Response', backref='attempt', lazy=True)
    
    def calculate_score(self) -> str:
        correct_responses = 0
        for response in self.responses: # type: ignore[attr-defined]
            if response.option.is_correct:
                correct_responses += 1
        total_questions = len(self.quiz.questions)
        self.score = correct_responses  # You can apply different scoring logic
        self.save()
        return f"You scored {self.score} out of {total_questions} questions"

    
    def __repr__(self):
        return f"<Attempt {self.id}>"
