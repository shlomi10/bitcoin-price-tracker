import json
import logging
from unittest.mock import Mock
import allure

from business_logic.tracker import BTCPriceTracker


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.suite("Tracker Logic")
@allure.feature("BTCPriceTracker.fetch_price")
def test_fetch_price(monkeypatch):
    logger.info("Running test_fetch_price")
    tracker = BTCPriceTracker("http://fake-api", "test.json")

    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {'data': {'amount': '29481.92'}}

    monkeypatch.setattr("requests.get", lambda url: mock_response)
    tracker.fetch_price()

    assert len(tracker.data) == 1
    assert isinstance(tracker.data[0]['price'], float)

@allure.feature("BTCPriceTracker.save_to_file")
def test_save_to_file(tmp_path):
    logger.info("Running test_save_to_file")
    test_file = tmp_path / "output.json"
    tracker = BTCPriceTracker("http://fake-api", str(test_file))
    tracker.data = [{"timestamp": "2025-01-01T00:00:00Z", "price": 100.0}]
    tracker.save_to_file()

    with open(test_file) as f:
        data = json.load(f)
    assert data[0]['price'] == 100.0
