import os
import socket
import subprocess
from flask import Flask, jsonify, render_template, request, redirect, flash, url_for
from dotenv import load_dotenv
from datetime import datetime

from app.monitor import get_system_info
from app.detector import detect_anomalies
from app.responder import respond_to
from static.reports.generate_report import parse_logs
from app.notifier import send_notification
from logs.logger import get_logger

load_dotenv()

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default-secret")

logger = get_logger()

@app.context_processor
def inject_today():
    return dict(today=datetime.now().strftime("%Y-%m-%d"))

@app.route("/")
def root():
    return jsonify({"message": "SentinelOps API en ligne"}), 200

@app.route("/status")
def status():
    info = get_system_info()
    return jsonify(info)

@app.route("/detect")
def detect():
    system_info = get_system_info()
    anomalies = detect_anomalies(system_info)
    return jsonify({"anomalies": anomalies})

@app.route("/respond")
def respond():
    system_info = get_system_info()
    anomalies = detect_anomalies(system_info)
    respond_to(anomalies)
    return jsonify({"response": "Traitement effectué."})

@app.route("/events")
def events():
    try:
        with open("logs/events.log", "r") as f:
            raw_lines = f.readlines()
        logs = [line.strip().split(" - ", 1) for line in raw_lines if " - " in line]
    except FileNotFoundError:
        logs = []
    return render_template("events.html", events=logs)

@app.route("/ui/events")
def ui_events():
    try:
        with open("logs/events.log", "r") as f:
            raw_lines = f.readlines()
        events = [line.strip().split(" - ", 1) for line in raw_lines if " - " in line]
    except FileNotFoundError:
        events = []
    return render_template("events.html", events=events)


@app.route("/report/generate")
def generate_report():
    try:
        subprocess.run(["python3", "static/reports/generate_report.py"], check=True)
        suffix = datetime.now().strftime("%Y-%m-%d")
        flash(f"✅ Rapport généré : report_{suffix}.html", "success")
        return redirect(url_for("view_report", date=suffix))
    except Exception as e:
        flash(f"❌ Erreur lors de la génération : {e}", "danger")
        return redirect(url_for("status"))

@app.route("/report/view/<date>")
def view_report(date):
    filename = f"report_{date}.html"
    return render_template("report_view.html", report_file=filename)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ui/status")
def ui_status():
    system_info = get_system_info()
    return render_template("status.html", data=system_info)

@app.route("/ui/test")
def ui_test():
    return render_template("ui_test.html")

@app.route("/ui/test/fake-alert", methods=["POST"])
def ui_fake_alert():
    fake_alert = {
        "type": "🧪 Test manuel (UI)",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Ceci est une alerte de test depuis l'interface.",
        "ip": socket.gethostbyname(socket.gethostname()),
        "hostname": socket.gethostname(),
    }
    send_notification(fake_alert)
    flash("✅ Alerte de test envoyée !", "success")
    return redirect("/ui/test")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
