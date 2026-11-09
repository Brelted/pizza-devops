from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "1.0")
    return f"<h1>🍕 Bienvenue chez Pizza DevOps</h1><p>Version {version}</p>"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    