import asyncio

from chathub.pipeline import run_pipeline, speak_with_interrupt


def test_pipeline_answers_every_message_in_order():
    spoken = asyncio.run(run_pipeline(["salut", "ça va ?"]))
    assert spoken == ["Réponse à : salut", "Réponse à : ça va ?"]


def test_pipeline_with_no_messages():
    assert asyncio.run(run_pipeline([])) == []


def test_speak_can_be_interrupted():
    text = "un deux trois quatre cinq"
    spoken = asyncio.run(speak_with_interrupt(text, word_delay=0.05, interrupt_after=0.12))
    assert 0 < len(spoken) < 5
    assert spoken == text.split()[: len(spoken)]


def test_speak_finishes_if_not_interrupted_in_time():
    spoken = asyncio.run(speak_with_interrupt("un deux", word_delay=0.01, interrupt_after=0.5))
    assert spoken == ["un", "deux"]
