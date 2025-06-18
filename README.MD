<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg" alt="Bitcoin Logo" width="100" />
</p>

# Bitcoin Price Tracker

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-green.svg?style=for-the-badge&logo=pytest)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-orange.svg?style=for-the-badge&logo=allure)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://docs.docker.com/compose/)
[![Allure Report](https://img.shields.io/badge/Allure%20Report-Live-purple?style=for-the-badge&logo=github)](https://shlomi10.github.io/bitcoin-price-tracker/)
[![CI](https://img.shields.io/github/actions/workflow/status/shlomi10/bitcoin-price-tracker/ci.yml?label=CI%20Build&style=for-the-badge&logo=github-actions)](https://github.com/shlomi10/bitcoin-price-tracker/actions/workflows/ci.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/shlomi10/bitcoin-tracker?style=for-the-badge)](https://hub.docker.com/r/shlomi10/bitcoin-tracker)
[![Docker Image Size](https://img.shields.io/docker/image-size/shlomi10/bitcoin-tracker/latest?style=for-the-badge)](https://hub.docker.com/r/shlomi10/bitcoin-tracker)

</div>

Track the current Bitcoin Price Index (BPI) in real-time using the Coinbase API.
Logs prices every minute, saves them to JSON, generates a graph, and emails the max value.

---

## 📦 Features
- Fetch Bitcoin price via Coinbase public API
- Store timestamped prices in JSON
- Generate graph (`matplotlib`)
- Send email with max price and chart
- Dockerized with Compose support
- Allure test reporting

---

## ✅ Test Coverage
- Pytest-based unit and integration tests
- Mocked API and SMTP behaviors
- Allure reporting for detailed execution logs

## 🚀 Usage

### 1. Clone & Configure
```bash
git clone https://github.com/shlomi10/bitcoin-price-tracker.git
cd bitcoin-price-tracker
cp .env.example .env
# Fill in SMTP/email credentials in .env
# Alternatively, set environment secrets in GitHub Actions for CI
```

### 2. Run tests locally
```bash
pytest tests/ --alluredir=allure-results
allure open allure-results
```

### 3. Run with Docker Compose
```bash
docker compose up --build
```

### 4. Run Tests with Allure
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

---

## 🐳 Docker Hub
Image available at:
[https://hub.docker.com/r/shlomi10/bitcoin-tracker](https://hub.docker.com/r/shlomi10/bitcoin-tracker)

```bash
docker pull shlomi10/bitcoin-tracker
```

---

## 🧪 Requirements
- Python 3.12+
- Docker + Docker Compose
- Allure CLI (for test reports): https://docs.qameta.io/allure/

---

## 📂 Project Structure
```
bitcoin-price-tracker/
├── business_logic/
│   └── tracker.py
│   └── logger.py
├── utils/
│   ├── graph_generator.py
│   └── email_sender.py
├── tests/
│   ├── test_tracker.py
│   ├── test_graph_generator.py
│   └── test_email_sender.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── main.py
```

---

## 📧 Maintainer
**Shlomi** — [Docker Hub](https://hub.docker.com/u/shlomi10) · [GitHub](https://github.com/shlomi10)
