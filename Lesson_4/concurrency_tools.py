
import asyncio

async def fake_call(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done."


async def main():

    # 1. Exécution séquentielle
    for n in "abc":
        await fake_call(n, 1)

    # 2. Exécution concurrente
    results = await asyncio.gather(
        fake_call("a", 1),
        fake_call("b", 1),
        fake_call("c", 1)
    )
    print(results)

    # 3. Création d'une tâche en arrière-plan
    task = asyncio.create_task(fake_call("bg", 1))
    result = await task
    print(result)

    # 4. Limitation du temps d'exécution
    try:
        await asyncio.wait_for(fake_call("slow", 5), timeout=2)
    except asyncio.TimeoutError:
        print("too slow")

    # 5. Limitation du nombre de tâches simultanées
    sem = asyncio.Semaphore(5)

    async def limited(coro_fn):
        async with sem:
            return await coro_fn()

    tasks = [
        limited(lambda: fake_call(f"task-{i}", 2))
        for i in range(10)
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )
    print(results)

    # 6. Exécution d'une fonction bloquante dans un thread
    # value = await asyncio.to_thread(blocking_fn, args)


asyncio.run(main())
