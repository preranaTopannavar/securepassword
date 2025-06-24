from flask import Flask, render_template, request
from utils import check_strength, check_breach

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        password = request.form["password"]
        strength_msg = check_strength(password)
        breach_msg = check_breach(password)
        message = strength_msg + " " + breach_msg
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
