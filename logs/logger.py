# logs/logger.py

import os
import logging
from logging.handlers import RotatingFileHandler

def get_logger(name='sentinel', log_path='logs/sentinel.log'):
    """
    Retourne un logger configuré avec rotation automatique.
    """
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    log_handler = RotatingFileHandler(
        log_path,
        maxBytes=500000,
        backupCount=3
    )

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    log_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(log_handler)

    return logger
