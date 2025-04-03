# monitor.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import psutil
import socket
import platform
from datetime import datetime
from logs.logger import get_logger

logger = get_logger()

def get_system_info():
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
        now = datetime.now()
        uptime = now - boot_time
        info['uptime'] = str(uptime).split('.')[0]

        # IP
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        info['hostname'] = hostname
        info['ip'] = ip_address

        # Système
        info['system'] = platform.system()
        info['release'] = platform.release()
        info['kernel'] = platform.version()

        logger.info("System status: %s", info)
        return info

    except Exception as e:
        logger.error("Erreur dans get_system_info: %s", str(e))
        return {'error': str(e)}

if __name__ == "__main__":
    from pprint import pprint
    pprint(get_system_info())
