# api.py

from flask import Flask, jsonify, render_template
from app.monitor import get_system_info
from app.detector import detect_anomalies
from logs.logger import get_logger

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

logger = get_logger()

@app.route("/")
def root():
    return jsonify({"message": "SentinelOps API en ligne"}), 200

@app.route("/status")
def status():
    data = get_system_info()
    return jsonify(data), 200

@app.route("/events")
def events():
    system_info = get_system_info()
    anomalies = detect_anomalies(system_info)
    return jsonify({"anomalies": anomalies}), 200

@app.route("/ui/status")
def ui_status():
    system_info = get_system_info()
    html = render_template("status.html", data=system_info)
    print("🚀 HTML rendu :")
    print(html)
    return html

@app.route("/ui/events")
def ui_events():
    system_info = get_system_info()
    anomalies = detect_anomalies(system_info)
    return render_template("events.html", anomalies=anomalies)


@app.route("/test")
def test_page():
    return render_template("test.html")


# Optionnel : pour vérif rapide
print("📍 Routes Flask disponibles :")
print(app.url_map)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
