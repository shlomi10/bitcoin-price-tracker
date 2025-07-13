import matplotlib.pyplot as plt
import json
from business_logic.logger import logger


"""
This class generates a graph from JSON data containing Bitcoin price and timestamps.
"""
class GraphGenerator:
    def generate(self, json_path, image_path):
        logger.info(f"Loading price data from {json_path}")
        with open(json_path, 'r') as f:
            data = json.load(f)
        timestamps = [item['timestamp'] for item in data]
        prices = [item['price'] for item in data]

        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, prices, marker='o')
        plt.xticks(rotation=45)
        plt.title("Bitcoin Price Index (Last Hour)")
        plt.xlabel("Timestamp")
        plt.ylabel("Price (USD)")
        plt.tight_layout()

        logger.info(f"Saving price graph to {image_path}")
        plt.savefig(image_path)
