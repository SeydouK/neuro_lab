import pytest

from chathub.store import MessageStore


def test_add_assigns_incrementing_ids():
    store = MessageStore()
    assert store.add("a", "one").id == 1
    assert store.add("b", "two").id == 2


def test_get_returns_message_or_raises_keyerror():
    store = MessageStore()
    msg = store.add("a", "one")
    assert store.get(msg.id) == msg
    with pytest.raises(KeyError):
        store.get(999)


def test_list_messages_all_and_limit():
    store = MessageStore()
    for i in range(5):
        store.add("a", f"msg {i}")
    assert [m.text for m in store.list_messages()] == [f"msg {i}" for i in range(5)]
    assert [m.text for m in store.list_messages(limit=2)] == ["msg 3", "msg 4"]
    assert store.list_messages(limit=0) == []


def test_delete_removes_message():
    store = MessageStore()
    msg = store.add("a", "one")
    store.delete(msg.id)
    with pytest.raises(KeyError):
        store.get(msg.id)


def test_delete_unknown_raises_keyerror():
    with pytest.raises(KeyError):
        MessageStore().delete(42)


def test_ids_are_not_reused_after_delete():
    store = MessageStore()
    first = store.add("a", "one")
    store.delete(first.id)
    assert store.add("a", "two").id == 2


def test_persistence_roundtrip(tmp_path):
    path = tmp_path / "messages.json"
    store = MessageStore(path)
    store.add("vedal", "hello")
    store.add("neuro", "hi")
    reloaded = MessageStore(path)
    assert [m.text for m in reloaded.list_messages()] == ["hello", "hi"]
    assert reloaded.add("x", "new").id == 3


def test_no_file_without_path(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    MessageStore().add("a", "b")
    assert list(tmp_path.iterdir()) == []
