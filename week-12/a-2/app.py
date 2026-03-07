# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "<h1>Bye Flask!</h1>"


@app.route("/username/<name>")
def learn(name):
    return f"Hello, <span style='color: blue; font-weight: bold;'>{name.title()}</span>, how are you doing today?"

@app.route("/username/<name>/<int:age>/<string:year>")
def learn_with_age(name, age, year):
    return f"Hello, <span style='color: blue; font-weight: bold;'>{name.title()}</span>, you are {age} years old and were born in {year}!"

@app.route("/profile/<name>")
def profile(name):
    
    return f"Hello, <span style='color: blue; font-weight: bold;'>{name.title()}</span>!"


if __name__ == "__main__":
    app.run(debug=True)
