# Exercice 1 : Await -> wait until this asynchronous operation finishes before continuing.
import asyncio 

async def cook():
    print("Cooking started...")
    await asyncio.sleep(3)
    print("Cooking finished!")

async def main():
    await cook()
    print("Now eating!")

asyncio.run(main())

# Exercice 2 : asyncio.create_task() -> Start a task in the background without waiting for it immediately
import asyncio 

async def cook_rice(): 
    print("Rice: started")
    await asyncio.sleep(3)
    print("Rice: finished")

async def main():
    task = asyncio.create_task(cook_rice())
    print("Preparing chicken...")
    await task 
    print("Dinner is ready!")

asyncio.run(main())

# Exercice 3: asyncio.gather() -> Execute several asynchronous operations concurrently and wait for all of them.
import asyncio 

async def fetch_api(name, delay): 
    print(f"{name}: started")
    await asyncio.sleep(delay)
    print(f"{name}: finished")
    return f"{name} data"

async def main():
    results = await asyncio.gather(
        fetch_api("API 1", 3), 
        fetch_api("API 2", 2),
        fetch_api("API 3", 1)
    )

    print(results)

asyncio.run(main())

# Exercice 4 : asyncio.wait_for() -> set a maximum time for an asynchronous operation 
import asyncio 

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(5)
    return "Data received!"

async def main(): 
    try: 
        result = await asyncio.wait_for(
        fetch_data(), 
        timeout=2
        )
        print(result)
    except asyncio.TimeoutError: 
        print("Request tined out!")

asyncio.run(main())

# Exercice 5 : asyncio.semaphore() -> Limit the number of operations running simultaneously 
import asyncio 

async def fetch_api(name, sem):
    async with sem: 
        print(f"{name} started.")
        await asyncio.sleep(2)
        print(f"{name} finished.")

async def main():
    sem = asyncio.Semaphore(3)

    tasks = [
        fetch_api(f"API {i}", sem)
        for i in range(1, 7)
    ]

    await asyncio.gather(*tasks)
asyncio.run(main())