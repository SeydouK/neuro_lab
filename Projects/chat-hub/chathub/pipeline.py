"""Pipeline asynchrone à la Neuro : chat -> cerveau -> voix (Leçon 4 : files d'attente, tâches, annulation).

Chaque étape tourne dans sa propre tâche et elles communiquent par des asyncio.Queue.
La valeur None dans une file est la SENTINELLE : "il n'y aura plus rien".
"""

import asyncio


async def chat_producer(queue: asyncio.Queue, messages: list[str], delay: float = 0.0) -> None:
    """Met chaque message dans la file (avec une pause de `delay` secondes entre chaque), puis None."""
    for message in messages: 
        await queue.put(message)
        await asyncio.sleep(delay)
    
    await queue.put(None)


async def brain(q_in: asyncio.Queue, q_out: asyncio.Queue, think_time: float = 0.0) -> None:
    """Lit les messages de q_in jusqu'à None. Pour chacun : attend think_time (le "LLM réfléchit"),
    puis met  f"Réponse à : {message}"  dans q_out. À la fin, met None dans q_out."""
    while True:
        message = await q_in.get()

        if message is None:
            break 

        await asyncio.sleep(think_time)

        response = f"Réponse à : {message}"
        await q_out.put(response)
    
    await q_out.put(None)


async def speaker(queue: asyncio.Queue, spoken: list[str]) -> None:
    """Lit les réponses de la file jusqu'à None et les ajoute à la liste `spoken`."""
    while True:
        response = await queue.get()

        if response is None: 
            break 

        spoken.append(response)


async def run_pipeline(messages: list[str], think_time: float = 0.0) -> list[str]:
    """Crée deux files, lance producer + brain + speaker EN CONCURRENCE (asyncio.gather),
    puis retourne la liste `spoken`."""
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()

    spoken = []

    await asyncio.gather(
        chat_producer(q1, messages),
        brain(q1, q2, think_time),
        speaker(q2, spoken)
    )

    return spoken


async def speak(text: str, word_delay: float, spoken_words: list[str]) -> None:
    """Dit le texte mot par mot : pour chaque mot (text.split()), attend word_delay puis l'ajoute à spoken_words."""
    for word in text.split():
        await asyncio.sleep(word_delay)
        spoken_words.append(word)


async def speak_with_interrupt(text: str, word_delay: float, interrupt_after: float) -> list[str]:
    """Lance speak() en tâche de fond, attend interrupt_after secondes, ANNULE la tâche
    (task.cancel(), puis await task en attrapant asyncio.CancelledError), et retourne
    les mots qui ont eu le temps d'être dits. C'est l'interruption d'un bot en pleine phrase."""
    spoken_words = []

    task = asyncio.create_task(
        speak(text, word_delay, spoken_words)
    )

    await asyncio.sleep(interrupt_after)

    task.cancel()

    try: 
        await task 
    except asyncio.CancelledError: 
        pass 

    return spoken_words

