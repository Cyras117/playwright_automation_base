import pytest,allure
from pages.home_page import HomePage
from playwright.async_api import Page

@allure.feature("Login")
@allure.story("Valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.asyncio
async def test_example(page:Page):
    pg = HomePage(page)
    await pg.open()

@pytest.mark.asyncio
async def test_dois(page:Page):
    await HomePage(page).open()
    await HomePage(page).go_to_docs()
    title = await HomePage(page).page.title()
    assert "Playwright" in title
