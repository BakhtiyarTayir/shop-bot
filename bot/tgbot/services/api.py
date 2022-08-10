
import aiohttp

URL = 'http://127.0.0.1:8000/api/v1/product/category/'
URL_CAT = 'http://127.0.0.1:8000/api/v1/product_list/'



async def get_cats():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return await response.json()

async def get_products(cat_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_CAT + str(cat_id)) as response:
            return await response.json()