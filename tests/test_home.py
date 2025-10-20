import pytest,allure
from utils.page_utils import check_title
from utils.general_utils import ALL_BROWSERS_DEVICES as platform
from pages.home_page import HomePage
from playwright.async_api import Page

@allure.feature('Login')
@allure.story('Valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.asyncio
@pytest.mark.parametrize(
    'page',[{'platform':p}for p in [platform['chrome'],platform['firefox'],platform['safari'],platform['edge'],platform['android'],platform['iphone']]],
      indirect=True)
async def test_example(page:Page):
    hp = HomePage(page)
    await hp.open()

@pytest.mark.asyncio
@pytest.mark.parametrize('page',[{'platform':p}for p in [platform['chrome'],platform['edge'],platform['firefox'],platform['safari'],platform['android'],platform['iphone']]], indirect=True)
async def test_page_title(page:Page):
    result = False
    hp = HomePage(page)
    await hp.open()
    result = await check_title(hp)
    assert result
    
