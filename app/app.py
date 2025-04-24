from flask import Flask
import os

app = Flask(__name__)

@app.route("/<path:filename>")
def serve_file(filename):
    name = os.getenv("APP_NAME", "Not_defined") # Use Conf name

    try:
        if ".." in filename or filename.startswith("/"):
            raise ValueError("Chemin non autorisé.")

        with open(f"static/{filename}") as f:
            content = f.read()
    except (FileNotFoundError, ValueError):
        content = "<p>No data found.</p>"
    if name == "Not_defined":
        return f"{content}"
    return f"<h1>{name}</h1>{content}"
@app.route("/")
def home():
    return "Utilise /nom_du_fichier pour charger un fichier HTML."

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)