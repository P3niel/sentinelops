# app/responder.py

import subprocess
from logs.logger import get_logger

logger = get_logger()

# --- Fonctions d'action définies en premier ---

def clean_tmp():
    try:
        subprocess.run(["rm", "-rf", "/tmp/*"], check=True)
        logger.info("🧹 Nettoyage du dossier /tmp exécuté.")
    except Exception as e:
        logger.error(f"Erreur lors du nettoyage de /tmp : {e}")

def free_memory():
    try:
        subprocess.run("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches", shell=True, check=True)
        logger.info("💾 Libération de la mémoire cache demandée.")
    except Exception as e:
        logger.error(f"Erreur libération mémoire : {e}")

# --- Dictionnaire de règles maintenant que les fonctions existent ---

RULES = {
    "CPU trop élevé": lambda: logger.info("Action suggérée : réduire charge ou notifier."),
    "RAM critique": free_memory,
    "Disque presque plein": clean_tmp,
}
print(RULES)
# --- Fonction principale d'exécution ---

def respond_to(anomalies: list):
    """
    Prend une liste d’anomalies, déclenche des actions associées si définies.
    """
    for alert in anomalies:
        logger.info(f"🚨 Anomalie détectée : {alert}")
        for pattern, action in RULES.items():
            if pattern in alert:
                logger.info(f"⚙️ Déclenchement action pour : {pattern}")
                try:
                    action()
                except Exception as e:
                    logger.error(f"Erreur dans l'action '{pattern}' : {e}")
