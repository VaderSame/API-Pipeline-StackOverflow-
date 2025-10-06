from flask import Blueprint, jsonify, request
from ..models import Question

question_bp = Blueprint("question_bp", __name__)

@question_bp.route("/questions", methods=["GET"])
def get_questions():
    tag = request.args.get("tag")
    score = request.args.get('min_score', type=int)
    query = Question.query
    if tag:
        query = query.filter(Question.tags.like(f"%{tag}%"))
    questions = query.all()
    if score:
        query = query.filter(Question.score >= score)
        
    return jsonify([q.as_dict() for q in query.all()])

