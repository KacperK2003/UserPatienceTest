from flask import render_template, make_response, redirect, url_for, request
from models import TestResult

def register_routes(app, db):
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
            return redirect(url_for('question1'))
        return render_template('test3.html')

    @app.route('/question1')
    def question1():
        cookie = request.cookies.get('question1_choice')
        if cookie:
            return redirect(url_for('submit'))
        return render_template('question1.html')

    @app.route('/submit')
    def submit():
        submitted = request.cookies.get('submitted')
        if submitted:
            return redirect(url_for('summary'))
    
        time1 = request.cookies.get('test1')
        if not time1:
            return redirect(url_for('test1'))
        time2 = request.cookies.get('test2')
        if not time2:
            return redirect(url_for('test2'))
        time3 = request.cookies.get('test3')
        if not time3:
            return redirect(url_for('test3'))
        question1_choice = request.cookies.get('question1_choice')
        if not question1_choice:
            return redirect(url_for('question1'))

        result = TestResult(
            test1=time1,
            test2=time2,
            test3=time3,
            question1_choice=question1_choice
        )

        db.session.add(result)
        db.session.commit()

        response = make_response(redirect(url_for('summary')))
        response.set_cookie('submitted', 'True')

        return response

    @app.route('/summary')
    def summary():
        time1 = request.cookies.get('test1')
        time2 = request.cookies.get('test2')
        time3 = request.cookies.get('test3')
        question1_choice = request.cookies.get('question1_choice')

        time1 = int(time1) if time1 else 0
        time2 = int(time2) if time2 else 0
        time3 = int(time3) if time3 else 0
       
        time1_in_seconds = round(time1 / 1000.0, 2)
        time2_in_seconds = round(time2 / 1000.0, 2)
        time3_in_seconds = round(time3 / 1000.0, 2)

        return render_template('summary.html', test1=time1_in_seconds, test2=time2_in_seconds, test3=time3_in_seconds,  question1_choice=question1_choice)
