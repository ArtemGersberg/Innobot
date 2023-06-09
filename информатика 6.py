from __future__ import annotations
import asyncio,aiohttp

def get_links_of_igames(answer):
    result=[]

    for i in range(len(answer)):
        result.append(answer[i]["url"])
    return result

async def request():
    link="https://api.thecatapi.com/v1/images/search?limit=10"

    session = aiohttp.ClientSession()

    response = await session.get(link)

    answer = await session
