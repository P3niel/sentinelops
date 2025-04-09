# app/detector.py
from datetime import datetime

def detect_anomalies(system_info: dict) -> list:
    anomalies = []

    if system_info["cpu_percent"] > 90:
        anomalies.append({
            "type": "CPU critique",
            "message": f"Utilisation CPU élevée ({system_info['cpu_percent']}%)",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hostname": system_info.get("hostname"),
            "ip": system_info.get("ip")
        })

    if system_info["ram_percent"] > 85:
        anomalies.append({
            "type": "RAM critique",
            "message": f"Utilisation RAM anormale ({system_info['ram_percent']}%)",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hostname": system_info.get("hostname"),
            "ip": system_info.get("ip")
        })

    if system_info["disk_percent"] > 90:
        anomalies.append({
            "type": "Disque presque plein",
            "message": f"Espace disque faible ({system_info['disk_percent']}%)",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hostname": system_info.get("hostname"),
            "ip": system_info.get("ip")
        })

    return anomalies
