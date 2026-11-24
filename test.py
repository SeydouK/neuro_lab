import asyncio 

async def test():
    print("This test has just started ...")
    await asyncio.sleep(3)
    print("The end!")

async def test_2():
    print("break!")
    await asyncio.sleep(10)

async def main():
    task = asyncio.create_task(test_2())

    await test()

    print("Task done:", task.done())
    print("Cancellation accepted:", task.cancel())

    try:
        await task
    except asyncio.CancelledError:
        print("Cancelled!")

asyncio.run(main())