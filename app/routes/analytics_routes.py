from flask import Blueprint, jsonify
from ..models import Question
from .. import db

analytics_bp = Blueprint("analytics_bp", __name__)

@analytics_bp.route("/stats" , methods = ["GET"])

def stats():
    total = Question.query.count()
    top = db.session.query(Question.tags, db.func.count(Question.id))\
        .group_by(Question.tags).order_by(db.func.count(Question.id).desc()).limit(5).all()
    return jsonify({
        "total_questions": total,
        "top_tags": [{"tags": t[0], "count": t[1]} for t in top]
    }) 