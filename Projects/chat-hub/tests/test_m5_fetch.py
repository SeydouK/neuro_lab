import asyncio
import time

import httpx

from chathub.fetch import fetch_many


def run_with(handler, urls, **kwargs):
    async def go():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            return await fetch_many(urls, client=client, **kwargs)

    return asyncio.run(go())


def test_results_keep_order_and_failures_are_returned_not_raised():
    def handler(request):
        if request.url.path.endswith("bad"):
            return httpx.Response(404)
        return httpx.Response(200, json={"name": request.url.path.strip("/")})

    urls = ["https://x.test/a", "https://x.test/bad", "https://x.test/c"]
    results = run_with(handler, urls)
    assert results[0] == {"name": "a"}
    assert isinstance(results[1], httpx.HTTPStatusError)
    assert results[2] == {"name": "c"}


def test_concurrency_is_limited():
    state = {"running": 0, "peak": 0}

    async def handler(request):
        state["running"] += 1
        state["peak"] = max(state["peak"], state["running"])
        await asyncio.sleep(0.02)
        state["running"] -= 1
        return httpx.Response(200, json={})

    urls = [f"https://x.test/{i}" for i in range(10)]
    results = run_with(handler, urls, max_concurrent=3)
    assert len(results) == 10
    assert 1 < state["peak"] <= 3


def test_requests_really_run_concurrently():
    async def handler(request):
        await asyncio.sleep(0.1)
        return httpx.Response(200, json={})

    urls = [f"https://x.test/{i}" for i in range(5)]
    start = time.perf_counter()
    run_with(handler, urls, max_concurrent=5)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.4  # 5 appels de 0,1 s : ~0,1 s en concurrence, 0,5 s en séquentiel
