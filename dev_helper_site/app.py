from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/python")
def python_page():
    return render_template("python.html")

@app.route("/git")
def git_page():
    return render_template("git.html")

@app.route("/mac")
def mac_page():
    return render_template("mac.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
