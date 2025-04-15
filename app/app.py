from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.getenv("APP_NAME", "Not_defined")
    try:
        with open("data.txt") as f:
            content = f.read()
    except FileNotFoundError:
        content = "No data found."
    return f"<h1>{name}</h1><p>{content}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
