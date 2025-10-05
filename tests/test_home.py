import pytest,allure
from pages.home_page import HomePage
from playwright.async_api import Page

@allure.feature("Login")
@allure.story("Valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "page",
    [{"browser": b, "device": d} for b in ["chromium", "firefox", "webkit"] for d in [None, "iPhone 12", "Pixel 5"]],
    indirect=True,
)
async def test_example(page:Page):
    pg = HomePage(page)
    await pg.open()

@pytest.mark.asyncio
@pytest.mark.parametrize("page",[{"browser":b,"device":None,"channel":None}for b in ["chromium", "firefox", "webkit"]], indirect=True)
async def test_dois(page:Page):
    await HomePage(page).open()
    await HomePage(page).go_to_docs()
    title = await HomePage(page).page.title()
    assert "Playwright" in title
    
