import pytest
from fastapi.testclient import TestClient

from chathub.api import create_app
from chathub.cli import main
from chathub.store import MessageStore


@pytest.fixture
def api_client(tmp_path):
    return TestClient(create_app(MessageStore(tmp_path / "messages.json")))


def test_post_then_list(api_client, capsys):
    assert main(["post", "vedal", "hello world"], client=api_client) == 0
    assert main(["list"], client=api_client) == 0
    out = capsys.readouterr().out
    assert "vedal" in out
    assert "hello world" in out


def test_list_limit(api_client, capsys):
    for i in range(3):
        main(["post", "a", f"msg{i}"], client=api_client)
    capsys.readouterr()
    main(["list", "--limit", "1"], client=api_client)
    out = capsys.readouterr().out
    assert "msg2" in out
    assert "msg0" not in out


def test_stats(api_client, capsys):
    main(["post", "vedal", "hello hello world"], client=api_client)
    capsys.readouterr()
    assert main(["stats", "--top", "1"], client=api_client) == 0
    out = capsys.readouterr().out
    assert "hello" in out
    assert "vedal" in out


def test_api_key_flag_and_errors(capsys):
    client = TestClient(create_app(MessageStore(), api_key="secret"))
    assert main(["post", "a", "b"], client=client) == 1
    assert "401" in capsys.readouterr().err
    assert main(["--api-key", "secret", "post", "a", "b"], client=client) == 0
