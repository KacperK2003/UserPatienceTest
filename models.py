from app import db

class TestResult(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    test1 = db.Column(db.Integer)
    test2 = db.Column(db.Integer)
    test3 = db.Column(db.Integer)
    question1_choice = db.Column(db.String)

    def __repr__(self):
        return f'<Result {self.id}>'