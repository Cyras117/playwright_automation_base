from playwright.async_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.docs_link = page.get_by_role("link", name="Docs")

    async def open(self):
        await self.page.goto("https://playwright.dev")

    async def go_to_docs(self):
        await self.docs_link.click()
