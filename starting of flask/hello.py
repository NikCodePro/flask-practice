from flask import Flask,render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/bye")
def say_bye():
    return '<h1>Bye</h1>'\
           '<p>this para</p>'



@app.route("/username/<name>/<int:num>")
def user(name, num):
    return f"Hello {name}, How's You. you are {num} year old"


if __name__ == "__main__":
    app.run(debug=True)