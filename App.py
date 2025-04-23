from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from os import getenv

from models import db, TestResult

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test1')
def test1():
    cookie = request.cookies.get('test1')
    if cookie:
        return redirect(url_for('test2'))
    
    return render_template('test1.html')

@app.route('/test2')
def test2():
    cookie = request.cookies.get('test2')
    if cookie:
        return redirect(url_for('test3'))
    
    return render_template('test2.html')

@app.route('/test3')
def test3():
    cookie = request.cookies.get('test3')
    if cookie:
        return redirect(url_for('summary'))
    return render_template('test3.html')

@app.route('/submit')
def submit():
    time1 = request.cookies.get('test1')
    if not time1:
        return redirect(url_for('test1'))
    time2 = request.cookies.get('test2')
    if not time2:
        return redirect(url_for('test2'))
    time3 = request.cookies.get('test3')
    if not time3:
        return redirect(url_for('test3'))
    
    submitted = request.cookies.get('submitted')
    if submitted:
        return redirect(url_for('summary'))
    
    result = TestResult(
        test1 = time1,
        test2 = time2,
        test3 = time3
    )

    db.session.add(result)
    db.session.commit()

    request.cookies.add('subbmited', 'True')

    return redirect(url_for('summary'))

@app.route('/summary')
def summary():
    return request.json

if __name__ == '__main__':
    load_dotenv()
    app.run(port=getenv('PORT'), debug=getenv('DEBUG'))