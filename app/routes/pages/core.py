# Flask modules
from flask import Blueprint, render_template, session

core_bp = Blueprint("core", __name__, url_prefix="/")


@core_bp.route("/")
def home_route():

    highest_score = session.get("highest_score", 0)
    return render_template("pages/home.html", highest_score=highest_score)
