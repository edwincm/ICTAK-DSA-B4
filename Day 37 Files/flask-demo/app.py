import pickle
from os import path
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template("hello.html")


@app.route("/result", methods=["POST"])
def result_page():
    sl = int(request.form["sl"])
    sw = int(request.form["sw"])
    pl = int(request.form["pl"])
    pw = int(request.form["pw"])

    file_name = "lr_model.pkl"
    with open(path.join("static", file_name), "rb") as f:
        lr_model = pickle.load(f)

    pred = lr_model.predict(np.array([[sl, sw, pl, pw]]))[0]

    return render_template("result.html", prediction=pred)


if __name__ == "__main__":
    app.run(debug=True)
