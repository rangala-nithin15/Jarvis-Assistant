from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/activate", methods=["POST"])
def activate():
    subprocess.Popen(["python", "jarvis.py"])
    return jsonify({"status": "JARVIS ONLINE"})

if __name__ == "__main__":
    app.run(debug=True)
