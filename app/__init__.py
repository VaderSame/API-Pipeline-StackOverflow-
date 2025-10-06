from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import and register blueprints
    from .routes.fetch_routes import fetch_bp
    from .routes.question_routes import question_bp
    from .routes.analytics_routes import analytics_bp

    app.register_blueprint(fetch_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(analytics_bp)

    with app.app_context():
        db.create_all()

    return app
