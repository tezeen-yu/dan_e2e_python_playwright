# dan_e2e_python_playwright

End-to-end (E2E) testing framework for APIs and web interfaces using [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/).

## Features

- E2E browser automation with Playwright (Chromium, Firefox, WebKit)
- API testing with custom API client fixtures
- Automatic test data cleanup between sessions
- Configurable browser selection via command line
- Allure reporting integration

## Project Structure

```
.
├── api/            # API client and endpoint wrappers
├── const/          # Constants used in tests
├── model/          # Page objects and models
├── tests/          # Test cases
├── utils/          # Utility functions
├── conftest.py     # Pytest fixtures and hooks
├── requirements.txt
├── pytest.ini
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) or `pip`
- Docker (optional, for services)

### Installation

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m playwright install

```

### Running Tests

```sh
pytest --browser=chromium
```

- Supported browsers: `chromium`, `firefox`, `webkit`
- Default browser is `chromium`

### Allure Reporting

To generate and view Allure reports:

```sh
pytest --alluredir=allure-results
allure serve allure-results
```

### Using Docker

The services are defined in `docker-compose.yml`:

```sh
docker-compose up -d
```

## Fixtures

- `browser_type`: Selects browser type from CLI
- `playwright`: Playwright instance
- `browser`: Browser instance
- `page`: New browser page (with data cleared)
- `api_client`: API client for HTTP requests
- `service_api`, `route_api`: API endpoint wrappers
- `clear_data`: Cleans up test data before each session

See [conftest.py](conftest.py) for details.

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

MIT
