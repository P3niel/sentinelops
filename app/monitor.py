# app/monitor.py

import psutil
import socket
import platform
from datetime import datetime
from logs.logger import get_logger

logger = get_logger()

def get_system_info() -> dict:
    """
    Récupère les informations système : CPU, RAM, disque, uptime, IP, etc.
    """
    info = {}

    try:
        # CPU
        info['cpu_percent'] = psutil.cpu_percent(interval=1)

        # RAM
        memory = psutil.virtual_memory()
        info['ram_total'] = round(memory.total / (1024 ** 2))
        info['ram_used'] = round(memory.used / (1024 ** 2))
        info['ram_percent'] = memory.percent

        # Disque
        disk = psutil.disk_usage('/')
        info['disk_total'] = round(disk.total / (1024 ** 3), 2)
        info['disk_used'] = round(disk.used / (1024 ** 3), 2)
        info['disk_percent'] = disk.percent

        # Uptime
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        info['uptime'] = str(uptime).split('.')[0]

        # IP & Hostname
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        info['hostname'] = hostname
        info['ip'] = ip

        # OS Info
        info['system'] = platform.system()
        info['release'] = platform.release()
        info['kernel'] = platform.version()

        logger.info("System status: %s", info)
        return info

    except Exception as e:
        logger.error("Erreur dans get_system_info: %s", str(e))
        return {"error": str(e)}
