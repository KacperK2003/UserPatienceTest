from flask import Flask, render_template, session, redirect, url_for, request
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

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

@app.route('/summary')
def summary():
    time1 = request.cookies.get('test1')
    if not time1:
        return redirect(url_for('test1'))
    time2 = request.cookies.get('test2')
    if not time2:
        return redirect(url_for('test2'))
    time3 = request.cookies.get('test3')
    if not time3:
        return redirect(url_for('test3'))
    return f'{time1}, {time2}, {time3}'

if __name__ == '__main__':
    load_dotenv()
    app.run(port=getenv('PORT'), debug=getenv('DEBUG'))