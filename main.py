# main.py

import sys
import os
from pprint import pprint

# 🔧 Ajout du chemin courant au PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.monitor import get_system_info
from app.detector import detect_anomalies
from app.responder import respond_to
from logs.logger import get_logger

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


if __name__ == "__main__":
    run_sentinel()

