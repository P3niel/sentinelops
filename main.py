# main.py

import sys
import os
import argparse
from pprint import pprint

# 🔧 Ajout du chemin courant au PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.monitor import get_system_info
from app.detector import detect_anomalies
from app.responder import respond_to
from app.notifier import send_notification  # pour le test
from logs.logger import get_logger
from datetime import datetime

logger = get_logger()

def run_sentinel():
    print("🌀 SentinelOps - Monitoring Intelligent Local\n")
    logger.info("🚀 Lancement SentinelOps...")

    # 📡 Étape 1 : Récupération des infos système
    system_info = get_system_info()
    print("📊 État système :")
    pprint(system_info)

    # 🧠 Étape 2 : Détection d’anomalies
    anomalies = detect_anomalies(system_info)

    if anomalies:
        print("\n🚨 Anomalies détectées :")
        for alert in anomalies:
            print(f" - {alert}")
        logger.info("🎯 Anomalies remontées pour réponse.")

        # 🛡️ Étape 3 : Réaction automatique
        respond_to(anomalies)
    else:
        print("\n✅ Aucun problème détecté.")
        logger.info("✅ Aucun problème détecté.")

    print("\n✅ Fin SentinelOps.\n")


def run_test_notification():
    print("📧 Test d'envoi d'une fausse alerte...")

    fake_alert = {
        "type": "🧪 Test manuel (CLI)",
        "message": "Simulation d’anomalie",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": "dojo-test",
        "ip": "127.0.0.1"
    }
    send_notification(fake_alert)

    print("✅ Email de test envoyé !")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SentinelOps - Surveillance système")
    parser.add_argument('--test', action='store_true', help="Envoyer une alerte de test par mail")

    args = parser.parse_args()

    if args.test:
        run_test_notification()
    else:
        run_sentinel()
