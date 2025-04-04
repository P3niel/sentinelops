# logs/logger.py

import os
import logging
from logging.handlers import RotatingFileHandler

def get_logger(name="sentinel", log_path="logs/sentinel.log"):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Évite les doublons

    log_path_abs = os.path.abspath(log_path)

    # Protection : éviter les handlers en double sans casser
    already_exists = False
    for h in logger.handlers:
        try:
            if isinstance(h, RotatingFileHandler) and h.baseFilename == log_path_abs:
                already_exists = True
                break
        except AttributeError:
            continue

    if not already_exists:
        log_handler = RotatingFileHandler(
            log_path, maxBytes=500000, backupCount=3
        )
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)

    return logger
