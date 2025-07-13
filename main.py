from business_logic.tracker import BTCPriceTracker
from utils.graph_generator import GraphGenerator
from utils.email_sender import EmailSender
from dotenv import load_dotenv
from business_logic.logger import logger
import os
import time
import json

"""
Main script for Bitcoin Price Tracker automation.

Responsibilities:
- Load environment variables (API endpoint, output paths, SMTP credentials)
- Initialize BTCPriceTracker and fetch Bitcoin prices periodically
- Save collected data to a JSON file
- Generate a graph of the Bitcoin Price Index over time
- Send an email with the maximum price and attached graph
"""

load_dotenv()

logger.info("Starting Bitcoin Tracker Script...")

tracker = BTCPriceTracker(
    api_url=os.getenv("API_URL"),
    output_file=os.getenv("OUTPUT_FILE")
)

logger.info("Initialized BTCPriceTracker")

for i in range(60):
    logger.info(f"Fetching price iteration {i+1}/60")
    tracker.fetch_price()
    time.sleep(60)

logger.info("Finished collecting prices. Saving to file...")
tracker.save_to_file()

graph_generator = GraphGenerator()
logger.info("Generating graph from collected data...")
graph_generator.generate(os.getenv("OUTPUT_FILE"), "btc_graph.png")
logger.info("Graph saved to btc_graph.png")

with open(os.getenv("OUTPUT_FILE"), 'r') as f:
    prices = [entry['price'] for entry in json.load(f)]
max_price = max(prices)
logger.info(f"Calculated max BTC price: ${max_price}")

email_sender = EmailSender()
logger.info(f"Sending email to {os.getenv('RECIPIENT_EMAIL')}")
email_sender.send(
    smtp_host=os.getenv("SMTP_HOST"),
    smtp_port=int(os.getenv("SMTP_PORT")),
    sender_email=os.getenv("SENDER_EMAIL"),
    password=os.getenv("SENDER_PASSWORD"),
    recipient_email=os.getenv("RECIPIENT_EMAIL"),
    subject="Bitcoin Max Price Report",
    body=f"The max BTC price in the last hour was: ${max_price}",
    attachment_path="btc_graph.png"
)
logger.info("Email sent successfully. Script completed.")
