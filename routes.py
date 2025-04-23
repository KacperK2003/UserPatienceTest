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
            return redirect(url_for('submit'))
        return render_template('test3.html')

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
    
        result = TestResult(
            test1 = time1,
            test2 = time2,
            test3 = time3
        )

        db.session.add(result)
        db.session.commit()

        response = make_response(redirect(url_for('summary')))
        response.set_cookie('submitted', 'True')

        return response

    @app.route('/summary')
    def summary():
        return request.json