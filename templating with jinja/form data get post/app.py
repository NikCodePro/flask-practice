from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/result/<score>')
def get_result(score):
    res = ""
    if score > 50:
        res = "Pass"
    else:
        res = "Fail"

    return render_template("result.html", res=res)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        ds = float(request.form['datascience'])
        total = science + maths + c + ds
        return url_for("get_result", score=total)


if __name__ == "__main__":
    app.run(debug=True)
