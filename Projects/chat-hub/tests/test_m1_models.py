from dataclasses import asdict, is_dataclass

from chathub.models import ChatMessage


def test_is_a_dataclass():
    assert is_dataclass(ChatMessage)


def test_default_values():
    msg = ChatMessage("vedal", "hello")
    assert msg.author == "vedal"
    assert msg.text == "hello"
    assert msg.id == 0
    assert isinstance(msg.created_at, str) and msg.created_at != ""


def test_equality():
    a = ChatMessage("vedal", "hi", id=1, created_at="2026-01-01T00:00:00")
    b = ChatMessage("vedal", "hi", id=1, created_at="2026-01-01T00:00:00")
    assert a == b


def test_asdict_has_four_fields():
    msg = ChatMessage("vedal", "hi")
    assert set(asdict(msg)) == {"author", "text", "id", "created_at"}
