# app/detector.py

from logs.logger import get_logger

logger = get_logger()

THRESHOLDS = {
    "cpu_percent": 90,
    "ram_percent": 85,
    "disk_percent": 90
}
def detect_anomalies(system_info: dict) -> list:
    anomalies = []

    if system_info.get("cpu_percent", 0) > THRESHOLDS["cpu_percent"]:
        anomalies.append(f"CPU trop élevé : {system_info['cpu_percent']}%")

    if system_info.get("ram_percent", 0) > THRESHOLDS["ram_percent"]:
        anomalies.append(f"RAM critique : {system_info['ram_percent']}%")

    if system_info.get("disk_percent", 0) > THRESHOLDS["disk_percent"]:
        anomalies.append(f"Disque presque plein : {system_info['disk_percent']}%")

    if anomalies:
        logger.warning("Anomalies détectées : %s", anomalies)

    return anomalies
