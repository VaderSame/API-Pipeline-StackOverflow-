import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///questions.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STACKEXCHANGE_API_URL = "https://api.stackexchange.com/2.3/questions"
