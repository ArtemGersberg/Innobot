import asyncio
from random import random
async def download_cat(i:int):
    await asyncio.sleep(random()*1.2)
    print(f"саt{i+1}.jpg")
async def request():
    link=...
    for i in range(10):
        await download_cat(i)

def main():
    asyncio.run(request())
main()

