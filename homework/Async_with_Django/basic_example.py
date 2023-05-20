import asyncio
import aiohttp

async def fetch_reddit_main_page():
    pass


async def fetch_facebook_main_page():
    pass

list_of_taaks = [
    fetch_facebook_main_page(),
    fetch_reddit_main_page(),.
]


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([list_of_tasks]))