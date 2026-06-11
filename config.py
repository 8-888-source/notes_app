class Config:
    SECRET_KEY = "very_secret_key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///notes.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False