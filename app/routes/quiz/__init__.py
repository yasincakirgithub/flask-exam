import random

# Flask modules
from flask import Blueprint, redirect, url_for, flash, render_template, request, session

# Local modules
from app.models.quiz import Question, AnswerType
from app.extensions import db, limiter
from app.forms.quiz import QuestionForm

quiz_bp = Blueprint("quiz", __name__, url_prefix="/quiz")


@quiz_bp.route("/", methods=["GET", "POST"])
def quiz_question_list():

    questions = Question.query.all()
    random_questions = random.sample(questions, min(5, len(questions)))
    highest_score = session.get("highest_score", 0)

    if request.method == "POST":
        score = 0
        for answered_question_key, user_answer in request.form.items():
            question_id = answered_question_key.split("question-")[-1]
            question_obj = Question.query.filter_by(id=question_id).first()
            if question_obj.ans == user_answer:
                score += 20

        if score > highest_score:
            session["highest_score"] = score

        flash(f"Your score is {score}")
        return redirect(url_for("pages.core.home_route"))

    return render_template("quiz/index.html", questions=random_questions, answer_type=AnswerType, highest_score=highest_score)
