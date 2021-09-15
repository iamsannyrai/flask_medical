import os.path
from datetime import datetime
import logging.handlers

BASE_PATH = os.getcwd()
LOG_FORMAT = '%(asctime)s %(filename)s %(message)s'

logger = logging.getLogger(__name__)

file_handler = logging.handlers.RotatingFileHandler(
    filename='{}/app_logs/{:%Y-%m-%d}'.format(BASE_PATH, datetime.now()),
    maxBytes=10000000)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(file_handler)
