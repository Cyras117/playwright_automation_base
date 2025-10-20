import time
async def check_title(page) -> bool:
    result = False
    title: str
    for _ in range(0,5,1):
        time.sleep(0.2)
        title = await page.page.title()
        result = 'pixsee' == title
        if result:
            break
    return result