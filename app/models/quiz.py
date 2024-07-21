# Local modules
from app.extensions import db
from app.utils.models import generate_uuid
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum


class AnswerType(Enum):
    single_line = "single_line"
    choice = "choice"
    yes_no = "yes_no"


class Question(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid, unique=True, nullable=False)
    queue = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    answer_type = db.Column(SQLAlchemyEnum(AnswerType), nullable=False)
    a = db.Column(db.String(255))
    b = db.Column(db.String(255))
    c = db.Column(db.String(255))
    d = db.Column(db.String(255))
    ans = db.Column(db.String(255))

    def __repr__(self):
        return f"<Question {self.text}>"
