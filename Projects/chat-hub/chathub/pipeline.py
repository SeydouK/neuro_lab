"""Pipeline asynchrone à la Neuro : chat -> cerveau -> voix (Leçon 4 : files d'attente, tâches, annulation).

Chaque étape tourne dans sa propre tâche et elles communiquent par des asyncio.Queue.
La valeur None dans une file est la SENTINELLE : "il n'y aura plus rien".
"""

import asyncio


async def chat_producer(queue: asyncio.Queue, messages: list[str], delay: float = 0.0) -> None:
    """Met chaque message dans la file (avec une pause de `delay` secondes entre chaque), puis None."""
    # TODO (M5)
    raise NotImplementedError


async def brain(q_in: asyncio.Queue, q_out: asyncio.Queue, think_time: float = 0.0) -> None:
    """Lit les messages de q_in jusqu'à None. Pour chacun : attend think_time (le "LLM réfléchit"),
    puis met  f"Réponse à : {message}"  dans q_out. À la fin, met None dans q_out."""
    # TODO (M5)
    raise NotImplementedError


async def speaker(queue: asyncio.Queue, spoken: list[str]) -> None:
    """Lit les réponses de la file jusqu'à None et les ajoute à la liste `spoken`."""
    # TODO (M5)
    raise NotImplementedError


async def run_pipeline(messages: list[str], think_time: float = 0.0) -> list[str]:
    """Crée deux files, lance producer + brain + speaker EN CONCURRENCE (asyncio.gather),
    puis retourne la liste `spoken`."""
    # TODO (M5)
    raise NotImplementedError


async def speak(text: str, word_delay: float, spoken_words: list[str]) -> None:
    """Dit le texte mot par mot : pour chaque mot (text.split()), attend word_delay puis l'ajoute à spoken_words."""
    # TODO (M5)
    raise NotImplementedError


async def speak_with_interrupt(text: str, word_delay: float, interrupt_after: float) -> list[str]:
    """Lance speak() en tâche de fond, attend interrupt_after secondes, ANNULE la tâche
    (task.cancel(), puis await task en attrapant asyncio.CancelledError), et retourne
    les mots qui ont eu le temps d'être dits. C'est l'interruption d'un bot en pleine phrase."""
    # TODO (M5)
    raise NotImplementedError
