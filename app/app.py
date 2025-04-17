from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.getenv("NAME", "Not_defined")
    try:
        with open("data.html") as f:
            content = f.read()
    except FileNotFoundError:
        content = "<p>No data found.</p>"
    return f"<h1>{name}</h1>{content}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
