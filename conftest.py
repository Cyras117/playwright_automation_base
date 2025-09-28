import pytest
from collections.abc import AsyncGenerator
from playwright.async_api import async_playwright,Playwright,Browser,Page


print("✅ Loading conftest.py ")

def pytest_configure(config:pytest.Config):
    print("✅ pytest_configure executed (conftest.py detected)")

@pytest.fixture(scope="session")
async def playwright_instance():
    async with async_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
async def browser(playwright_instance:Playwright,pytestconfig:pytest.Config):
    browser_name = pytestconfig.getoption("--browser")
    for name in browser_name:
        browser = await getattr(playwright_instance, name).launch()
        # browser = await playwright_instance.chromium.launch(headless=False) 
        # browser = await playwright_instance.firefox.launch(headless=False)
        yield browser
        await browser.close()
    

@pytest.fixture
async def page(browser:Browser)-> AsyncGenerator[Page, None]:
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()


