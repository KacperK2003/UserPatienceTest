from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test1 = db.Column(db.Integer)
    test2 = db.Column(db.Integer)
    test3 = db.Column(db.Integer)