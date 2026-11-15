"""Appels HTTP asynchrones vers des API externes (Leçon 3 : httpx, Leçon 4 : gather/Semaphore)."""

import asyncio

import httpx


async def fetch_json(client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore) -> dict:
    """GET sur l'url, à l'intérieur de `async with sem:` (pour limiter les requêtes simultanées).
    Lève une exception si le statut est 4xx/5xx (r.raise_for_status()), sinon retourne r.json()."""
    # TODO (M5)
    raise NotImplementedError


async def fetch_many(
    urls: list[str],
    max_concurrent: int = 5,
    timeout: float = 3.0,
    client: httpx.AsyncClient | None = None,
) -> list[dict | BaseException]:
    """Récupère toutes les urls EN CONCURRENCE, au plus `max_concurrent` en même temps.

    - Les résultats reviennent dans le même ordre que les urls.
    - Une url qui échoue ne fait PAS planter les autres : son résultat est l'exception
      (indice : asyncio.gather(..., return_exceptions=True)).
    - client=None -> créer httpx.AsyncClient(timeout=timeout) et le refermer à la fin (await client.aclose()).
      Si un client est fourni (tests), l'utiliser sans le refermer.
    """
    # TODO (M5)
    raise NotImplementedError
