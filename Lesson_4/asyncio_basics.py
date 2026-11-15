import asyncio

async def fake_call(name:str, delay:float) -> str: 
    await asyncio.sleep(delay)
    return f"{name} done."

async def main():
    for n in "abc":
        await fake_call(n, 1)
    
    results = await asyncio.gather(fake_call("a",1), fake_call("b", 1), fake_call("c", 1))
    print(results)

asyncio.run(main())