import pytest
from playwright.sync_api import sync_playwright
from api.api_client import APIClient
from api.route_api import RouteAPI
from api.service_api import ServiceAPI


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests: chromium, firefox, webkit"
    )

@pytest.fixture(scope="session")
def browser_type(pytestconfig):
    return pytestconfig.getoption("browser")

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright, browser_type):
    browser = getattr(playwright, browser_type).launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def page(browser, clear_data):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    page.close()

@pytest.fixture(scope="session")
def api_client(playwright) -> APIClient:
    request_context = playwright.request.new_context()
    return APIClient(request_context, base_url="http://localhost:8001")

@pytest.fixture(scope="session")
def service_api(api_client) -> ServiceAPI:
    return ServiceAPI(api_client)

@pytest.fixture(scope="session")
def route_api(api_client) -> RouteAPI:
    return RouteAPI(api_client)

@pytest.fixture(scope="session", autouse=True)
def clear_data(service_api, route_api):
    route_api.delete_all()
    service_api.delete_all()
