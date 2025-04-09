# app/responder.py

from datetime import datetime
import subprocess
from app.monitor import get_system_info
from logs.logger import get_logger, get_event_logger
from app.notifier import send_notification

logger = get_logger()
event_logger = get_event_logger()

# --- 🔧 Actions système ---

def clean_tmp():
    try:
        subprocess.run(["rm", "-rf", "/tmp/*"], check=True)
        logger.info("🧹 Nettoyage du dossier /tmp exécuté.")
    except Exception as e:
        logger.error(f"❌ Erreur nettoyage /tmp : {e}")

def free_memory():
    try:
        subprocess.run("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches", shell=True, check=True)
        logger.info("💾 Mémoire cache libérée.")
    except Exception as e:
        logger.error(f"❌ Erreur libération mémoire : {e}")

# --- 🧠 Mapping règles anomalies → actions

RULES = {
    "CPU trop élevé": lambda: logger.info("⚠️ CPU élevé – action manuelle recommandée."),
    "RAM critique": free_memory,
    "Disque presque plein": clean_tmp,
}

# --- 🧠 Détection type alerte pour enrichir notif

def detect_alert_type(message):
    message = message.lower()
    if "cpu" in message:
        return "CPU"
    elif "ram" in message or "mémoire" in message:
        return "Mémoire"
    elif "disque" in message or "disk" in message:
        return "Disque"
    elif "sshd" in message or "ssh" in message:
        return "Service SSH"
    else:
        return "Inconnu"

# --- 🧠 Fonction principale : réponse + notification

def respond_to(anomalies: list):
    system_info = get_system_info()
    
    for alert in anomalies:
        event_logger.info(alert)

        # 🔁 Exécution de l’action associée (si règle connue)
        for pattern, action in RULES.items():
            if pattern in alert:
                logger.info(f"⚙️ Déclenchement action pour : {pattern}")
                try:
                    action()
                except Exception as e:
                    logger.error(f"❌ Erreur dans l'action '{pattern}' : {e}")
                break

        # 📬 Préparation notification enrichie
        notification_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": detect_alert_type(alert),
            "message": alert,
            "hostname": system_info.get("hostname", "inconnu"),
            "ip": system_info.get("ip", "inconnue")
        }

        send_notification(notification_data)
