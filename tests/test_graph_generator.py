import json
import logging
import allure
from utils.graph_generator import GraphGenerator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.suite("Graph Generation")
@allure.feature("generate_graph")
def test_generate_graph(tmp_path):
    logger.info("Running test_generate_graph")
    json_path = tmp_path / "input.json"
    image_path = tmp_path / "graph.png"

    sample_data = [
        {"timestamp": "2025-01-01T00:00:00Z", "price": 100},
        {"timestamp": "2025-01-01T01:00:00Z", "price": 150}
    ]

    with open(json_path, 'w') as f:
        json.dump(sample_data, f)

    generator = GraphGenerator()
    generator.generate(str(json_path), str(image_path))
    assert image_path.exists()
