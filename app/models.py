from . import db

class Question(db.Model):
    class Question(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        link = db.Column(db.String, nullable=False)
        is_answered = db.Column(db.Boolean)
        score = db.Column(db.Integer)
        tags = db.Column(db.String)
    
    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "link": self.link,
            "is_answered": self.is_answered,
            "score": self.score,
            "tags": self.tags
        }