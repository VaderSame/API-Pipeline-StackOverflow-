from flask import Blueprint, jsonify
from ..models import Question
from ..services.stackexchange_service import fetch_stackexchange_questions
from .. import db

fetch_bp = Blueprint("fetch_bp", __name__)

@fetch_bp.route("/fetch", methods=["POST"])
def fetch_questions():
    data = fetch_stackexchange_questions()
    added = 0
    for q in data:
        if q["answer_count"] == 0 and not Question.query.get(q["question_id"]):
            question = Question(
                id=q["question_id"],
                title=q["title"],
                link=q["link"],
                is_answered=q["is_answered"],
                score=q["score"],
                tags=",".join(q["tags"])
            )
            db.session.add(question)
            added += 1
    db.session.commit()
    return jsonify({"message": f"Added {added} new questions"})
