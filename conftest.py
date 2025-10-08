import pytest
from collections.abc import AsyncGenerator
from playwright.async_api import async_playwright,Playwright,Browser,Page,BrowserContext


ALL_BROWSERS_DEVICES = {
    "chrome":{
        "browser":"chromium",
        "channel":"chrome",
        "device":None
    },
    "edge":{
        "browser":"chromium",
        "channel":"msedge",
        "device":None
    },
    "firefox":{
        "browser":"firefox",
        "channel":None,
        "device":None
    },
    "safari":{
        "browser":"webkit",
        "channel":None,
        "device":None
    },
    "iphone":{
        "browser":"webkit",
        "channel":None,
        "device":"iPhone 12"
    },
    "android":{
        "browser":"chromium",
        "channel":"chrome",
        "device":"Galaxy S24"
    }
}

def pytest_addoption(parser):
    parser.addoption(
        "--channel",
        action="store",
        default=None,
        help="Browser channel to use (e.g., chrome, msedge). Only valid with chromium."
    )

def pytest_configure():
    print("✅ pytest_configure executed (conftest.py detected)")

@pytest.fixture(scope="session")
async def playwright_instance():
    async with async_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
async def page(playwright_instance:Playwright,pytestconfig:pytest.Config,request):
    #Get headed param
    headed = False if pytestconfig.getoption("headed") else True

    #Seting browser context
    context: BrowserContext
    platform = request.param.get("platform")
    browser_name = platform.get("browser")
    channel_name = platform.get("channel")
    device_name = platform.get("device")

    browser_type = getattr(playwright_instance, browser_name)
    browser: Browser = await browser_type.launch(headless=headed,channel=channel_name)

    #checking if there is device
    if device_name:
        device = playwright_instance.devices[device_name]
        context = await browser.new_context(**device)
    else:
        context = await browser.new_context()

    page:Page = await context.new_page()

    #Yield page for the test
    yield page
    await context.close() 

    
