from re import U


import aiohttp

URL = 'http://127.0.0.1:8000/api/v1/product/category/'


async def get_cats():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return await response.json()
