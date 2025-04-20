from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=getenv('DEBUG'))