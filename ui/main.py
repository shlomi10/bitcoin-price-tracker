from fastapi import FastAPI, BackgroundTasks
import time, json, os
from business_logic.tracker import BTCPriceTracker
from utils.graph_generator import GraphGenerator
from utils.email_sender import EmailSender
from dotenv import load_dotenv
from business_logic.logger import logger

load_dotenv()
app = FastAPI()

def collect_and_email():
    logger.info("Starting BTC price tracking for 60 minutes...")
    tracker = BTCPriceTracker(
        api_url=os.getenv("API_URL"),
        output_file=os.getenv("OUTPUT_FILE")
    )
    for _ in range(60):
        tracker.fetch_price()
        time.sleep(60)

    logger.info("Finished tracking. Saving data...")
    tracker.save_to_file()

    logger.info("Generating graph...")
    GraphGenerator().generate(os.getenv("OUTPUT_FILE"), "btc_graph.png")

    with open(os.getenv("OUTPUT_FILE"), "r") as f:
        prices = [p["price"] for p in json.load(f)]
    max_price = max(prices)

    logger.info(f"Graph saved to btc_graph.png. Sending email to {os.getenv('RECIPIENT_EMAIL')}")
    EmailSender().send(
        smtp_host=os.getenv("SMTP_HOST"),
        smtp_port=int(os.getenv("SMTP_PORT")),
        sender_email=os.getenv("SENDER_EMAIL"),
        password=os.getenv("SENDER_PASSWORD"),
        recipient_email=os.getenv("RECIPIENT_EMAIL"),
        subject="Bitcoin Max Price Report",
        body=f"Max BTC price in the last hour: ${max_price}",
        attachment_path="btc_graph.png",
    )
    logger.info("Email sent successfully.")

@app.post("/track-hour")
def start_hourly_tracking(tasks: BackgroundTasks):
    tasks.add_task(collect_and_email)
    return {"status": "collection started"}

