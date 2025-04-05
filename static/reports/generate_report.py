import os
import re
from datetime import datetime

# 📄 Chemin du fichier log
LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../logs/sentinel.log"))

# 📁 Dossier de sortie
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../reports"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 📅 Suffixe de date
DATE_SUFFIX = datetime.now().strftime("%Y-%m-%d")

# 📦 Fichiers générés
HTML_NAME = f"report_{DATE_SUFFIX}.html"
CSV_NAME = f"report_{DATE_SUFFIX}.csv"
HTML_PATH = os.path.join(OUTPUT_DIR, HTML_NAME)
CSV_PATH = os.path.join(OUTPUT_DIR, CSV_NAME)


# 📊 Parser log CSV-like (timestamp,level,message)

def parse_logs():
    if not os.path.exists(LOG_PATH):
        print("⚠️ Fichier de logs introuvable.")
        return []

    with open(LOG_PATH, "r") as f:
        lines = f.readlines()

    entries = []
    log_pattern = re.compile(r"^(.*?)\s+\[(.*?)\]\s+(.*)$")  # timestamp [LEVEL] message

    for line in lines:
        line = line.strip()
        if not line:
            continue

        match = log_pattern.match(line)
        if match:
            timestamp, level, message = match.groups()
            level = level.upper().strip()
            entries.append((timestamp.strip(), level, message.strip()))
    return entries



# 📝 Export CSV
def export_csv(entries):
    with open(CSV_PATH, "w") as f:
        f.write("Timestamp,Level,Message\n")
        for entry in entries:
            f.write(f"{entry[0]},{entry[1]},{entry[2]}\n")
    print(f"✅ CSV généré : {CSV_PATH}")


# 🌐 Export HTML avec JS collapsible pour messages riches
def export_html(entries):
    with open(HTML_PATH, "w") as f:
        f.write("<html><head><title>Rapport SentinelOps</title>")
        f.write('<link rel="stylesheet" href="/static/css/report.css">')
        f.write("""
        <script>
        function toggleDetails(id) {
            const el = document.getElementById(id);
            el.style.display = el.style.display === 'none' ? 'block' : 'none';
        }
        </script>
        """)
        f.write("</head><body>")
        f.write(f"<h2>📄 Rapport SentinelOps — {DATE_SUFFIX}</h2>")
        f.write("<table><tr><th>Timestamp</th><th>Niveau</th><th>Message</th></tr>")

        for i, entry in enumerate(entries):
            level_class = entry[1].lower()
            timestamp, level, message = entry

            # 🎯 Repli automatique si message > 100 caractères
            if len(message) > 100:
                collapsed_id = f"details-{i}"
                preview = message[:80].strip() + "..."
                message_html = f"""
                <span>{preview}</span>
                <button onclick="toggleDetails('{collapsed_id}')" style="margin-left: 10px;">Voir +</button>
                <pre id="{collapsed_id}" style="display:none; margin:0; padding:5px;">{message}</pre>
                """
            else:
                message_html = message

            f.write(f'<tr class="{level_class}"><td>{timestamp}</td><td>{level}</td><td>{message_html}</td></tr>')
            level_class = "info"
            if "WARN" in level:
                level_class = "warning"
            elif "ERROR" in level:
                level_class = "error"


        f.write("</table></body></html>")
    print(f"✅ HTML généré : {HTML_PATH}")



# 🧪 Debug initial
print("🧪 Chemin résolu :", LOG_PATH)
print("🧪 Fichier existe ?", os.path.exists(LOG_PATH))


# 🚀 Exécution principale
if __name__ == "__main__":
    entries = parse_logs()
    if entries:
        export_csv(entries)
        export_html(entries)
    else:
        print("ℹ️ Aucun log à traiter.")
