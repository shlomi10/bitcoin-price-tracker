from fastapi import FastAPI, BackgroundTasks
import time, json, os
from business_logic.tracker import BTCPriceTracker
from utils.graph_generator import GraphGenerator
from utils.email_sender import EmailSender
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

def collect_and_email():
    tracker = BTCPriceTracker(
        api_url=os.getenv("API_URL"),
        output_file=os.getenv("OUTPUT_FILE")
    )
    for _ in range(60):
        tracker.fetch_price()
        time.sleep(60)

    tracker.save_to_file()
    GraphGenerator().generate(os.getenv("OUTPUT_FILE"), "btc_graph.png")

    with open(os.getenv("OUTPUT_FILE"), "r") as f:
        prices = [p["price"] for p in json.load(f)]
    max_price = max(prices)

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

@app.post("/track-hour")
def start_hourly_tracking(tasks: BackgroundTasks):
    tasks.add_task(collect_and_email)
    return {"status": "collection started"}
