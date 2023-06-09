import asyncio

def f():
    x = int(input())
    return x

async def Lound(x):
    print("начали стирку")
    await asyncio.sleep(1*x)
    print("закончили стирку")


async def Tea(x):
    print("поставили чайник")
    await asyncio.sleep(0.75*x)
    print("чайник вскипел")



async def Wed(x):
    print("поставили овощи")
    await asyncio.sleep(5*x)
    print("овощи готовы")


async def main():
    x = f()
    await asyncio.gather(Wed(x),Tea(x),Lound(x))

asyncio.run(main())








