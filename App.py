from flask import Flask
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=getenv('DEBUG'))