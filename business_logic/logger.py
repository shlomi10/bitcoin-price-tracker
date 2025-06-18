import logging

"""
Configures and exposes the logger used across the application.
"""
logger = logging.getLogger("BTC_Logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("btc.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
