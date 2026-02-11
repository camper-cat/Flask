from flask import Flask, render_template, request, redirect

app = Flask(__name__)
notes = []


# ----------- pages -----------

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


@app.route("/notes")
def notes_page():
    return render_template("notes.html", notes=notes)


# ----------- GET ------------

@app.route("/get_data")
def get_data():
    name = request.args.get("name")
    topic = request.args.get("topic")
    return f"GET Request received: {name} - {topic}"


# ----------- POST -----------

@app.route("/post_data", methods=["POST"])
def post_data():
    note = request.form.get("comment")

    if note:
        notes.append(note)

    return redirect("/notes")

# ----------- PUT -----------

@app.route("/put_data", methods=["PUT"])
def put_data():
    data = request.get_json()
    return jsonify({"method": "PUT", "received": data})


# ----------- PATCH -----------

@app.route("/patch_data", methods=["PATCH"])
def patch_data():
    data = request.get_json()
    return jsonify({"method": "PATCH", "received": data})


# ----------- DELETE -----------

@app.route("/delete_data", methods=["DELETE"])
def delete_data():
    data = request.get_json()
    return jsonify({"method": "DELETE", "received": data})

@app.route("/delete_note/<int:index>", methods=["DELETE"])
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return "deleted"

@app.route("/update_note/<int:index>", methods=["PUT"])
def update_note(index):
    data = request.get_json()
    new_text = data.get("text")

    if 0 <= index < len(notes) and new_text:
        notes[index] = new_text

    return "updated"


# ----------- RUN SERVER -----------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
