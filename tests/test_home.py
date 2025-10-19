import pytest,allure
from conftest import ALL_BROWSERS_DEVICES as platform
from pages.home_page import HomePage
from playwright.async_api import Page

@allure.feature("Login")
@allure.story("Valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "page",[{"platform":p}for p in [platform["chrome"],platform["firefox"],platform["safari"],platform["edge"],platform["android"],platform["iphone"]]],
      indirect=True)
async def test_example(page:Page):
    pg = HomePage(page)
    await pg.open()

@pytest.mark.asyncio
@pytest.mark.parametrize("page",[{"platform":p}for p in [platform.get("chrome"),platform.get("edge")]], indirect=True)
async def test_dois(page:Page):
    await HomePage(page).open()
    await HomePage(page).go_to_docs()
    title = await HomePage(page).page.title()
    assert "Playwright" in title
    
