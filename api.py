import os
import subprocess
import datetime  # module complet utilisé pour éviter les conflits
from flask import Flask, flash, jsonify, redirect, render_template, url_for

# Modules internes
from app.monitor import get_system_info
from app.detector import detect_anomalies
from logs.logger import get_logger

# 📁 Initialisation de l’application Flask
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))
app.secret_key = "sentinelops-dev-key"  # 🔐 À sécuriser en prod

# 📚 Logger
logger = get_logger()

# 🧭 Injection de la date actuelle dans tous les templates
@app.context_processor
def inject_today():
    return dict(today=datetime.datetime.now().strftime("%Y-%m-%d"))

# 🌐 Route de test API
@app.route("/")
def root():
    return jsonify({"message": "SentinelOps API en ligne"}), 200

# 🔎 Données système brutes (JSON)
@app.route("/status")
def status():
    data = get_system_info()
    return jsonify(data), 200

# 🚨 Détection d’anomalies (JSON)
@app.route("/events")
def events():
    system_info = get_system_info()
    anomalies = detect_anomalies(system_info)
    return jsonify({"anomalies": anomalies}), 200

# 🌐 UI : statut système
@app.route("/ui/status")
def ui_status():
    system_info = get_system_info()
    return render_template("status.html", data=system_info)

# 🌐 UI : affichage des événements logs
@app.route("/ui/events")
def ui_events():
    try:
        with open("logs/events.log", "r") as f:
            raw_lines = f.readlines()
        events = [line.strip().split(" - ", 1) for line in raw_lines if " - " in line]
    except FileNotFoundError:
        events = []
    return render_template("events.html", events=events)

# 📄 Génération de rapport depuis l’interface
@app.route("/report/generate")
def generate_report():
    try:
        subprocess.run(["python3", "static/reports/generate_report.py"], check=True)
        suffix = datetime.datetime.now().strftime("%Y-%m-%d")
        flash(f"✅ Rapport généré : report_{suffix}.html", "success")
        return redirect(url_for("view_report", date=suffix))
    except Exception as e:
        flash(f"❌ Erreur lors de la génération : {e}", "danger")
        return redirect(url_for("ui_status"))

# 🌐 Affichage du rapport généré (HTML via iframe)
@app.route("/report/view/<date>")
def view_report(date):
    filename = f"report_{date}.html"
    return render_template("report_view.html", report_file=filename)

# 🚀 Lancement du serveur Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
