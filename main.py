from business_logic.tracker import BTCPriceTracker
from utils.graph_generator import generate_graph
from utils.email_sender import send_email
from dotenv import load_dotenv
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

tracker = BTCPriceTracker(
    api_url=os.getenv("API_URL"),
    output_file=os.getenv("OUTPUT_FILE")
)

for _ in range(2):
    tracker.fetch_price()
    time.sleep(2)

tracker.save_to_file()
generate_graph(os.getenv("OUTPUT_FILE"), "btc_graph.png")

with open(os.getenv("OUTPUT_FILE"), 'r') as f:
    prices = [entry['price'] for entry in json.load(f)]
max_price = max(prices)

send_email(
    smtp_host=os.getenv("SMTP_HOST"),
    smtp_port=int(os.getenv("SMTP_PORT")),
    sender_email=os.getenv("SENDER_EMAIL"),
    password=os.getenv("SENDER_PASSWORD"),
    recipient_email=os.getenv("RECIPIENT_EMAIL"),
    subject="Bitcoin Max Price Report",
    body=f"The max BTC price in the last hour was: ${max_price}",
    attachment_path="btc_graph.png"
)


