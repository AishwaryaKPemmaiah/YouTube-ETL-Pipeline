import logging
from google.cloud import logging as cloud_logging

def setup_logging():
    client = cloud_logging.Client()
    client.setup_logging()
    logger = logging.getLogger("youtube_etl")
    logger.setLevel(logging.INFO)
    return logger

def log_info(message):
    logger = setup_logging()
    logger.info(message)

def log_error(message):
    logger = setup_logging()
    logger.error(message)