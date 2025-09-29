import pytest
from collections.abc import AsyncGenerator
from playwright.async_api import async_playwright,Playwright,Browser,Page


def pytest_addoption(parser):
    parser.addoption(
        "--channel",
        action="store",
        default=None,
        help="Browser channel to use (e.g., chrome, msedge). Only valid with chromium."
    )

def pytest_configure(config:pytest.Config):
    print("✅ pytest_configure executed (conftest.py detected)")

@pytest.fixture(scope="session")
async def playwright_instance():
    async with async_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
async def browser(playwright_instance:Playwright,pytestconfig:pytest.Config):
    browser_name = pytestconfig.getoption("browser")
    headed = False if pytestconfig.getoption("headed") else True
    browser_channel = pytestconfig.getoption("channel")
    device_name= pytestconfig.getoption("device")
    
    if browser_name:
        browser_name = browser_name[0]
        if browser_name == "chromium" and browser_channel:
            browser_type = getattr(playwright_instance, browser_name)
            browser = await browser_type.launch(channel=browser_channel, headless=headed)
            yield browser
            await browser.close()
        else:
            browser_type = getattr(playwright_instance, browser_name)
            browser = await browser_type.launch(headless=headed)
            yield browser
            await browser.close()
    elif device_name:
        device = playwright_instance.devices[device_name]
        browser_type = getattr(playwright_instance, device['default_browser_type'])
        browser = await browser_type.launch(headless=headed)
        yield browser
        await browser.close()
    else:
        print("Invalid browser/device args...")


@pytest.fixture
async def page(browser:Browser,playwright_instance:Playwright,pytestconfig:pytest.Config)-> AsyncGenerator[Page, None]:
    context = None
    device_name= pytestconfig.getoption("device")
    if device_name:
        device = playwright_instance.devices[device_name]
        context = await browser.new_context(**device)
        page = await context.new_page()
        yield page
        await context.close()
    else:
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()


