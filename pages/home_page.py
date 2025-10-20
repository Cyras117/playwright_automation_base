from utils.general_utils import BASE_URL,ROUTES
from playwright.async_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_route =  ROUTES['home']
        self.base_url = f'{BASE_URL}{self.base_route}'

    async def open(self):
        await self.page.goto(self.base_url, wait_until='load')

    # async def go_to_docs(self):
    #     await self.docs_link.click()
 