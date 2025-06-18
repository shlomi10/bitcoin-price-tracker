import requests
import json
from datetime import datetime, UTC
from business_logic.logger import logger

"""
Fetches, stores, and persists Bitcoin price data from a public API.
"""
class BTCPriceTracker:
    def __init__(self, api_url, output_file):
        self.api_url = api_url
        self.output_file = output_file
        self.data = []

    def fetch_price(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            price = float(response.json()['data']['amount'])
            timestamp = datetime.now(UTC).isoformat()
            logger.info(f"Fetched BTC price: {price}")
            self.data.append({"timestamp": timestamp, "price": price})
        except Exception as e:
            logger.error(f"Failed to fetch BTC price: {e}")

    def save_to_file(self):
        with open(self.output_file, 'w') as f:
            json.dump(self.data, f, indent=2)
        logger.info("Saved price data to JSON")
