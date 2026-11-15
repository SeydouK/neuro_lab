import pytest


@pytest.fixture(autouse=True)
def _no_api_key_env(monkeypatch):
    """Les tests ne doivent pas dépendre de ta variable d'environnement."""
    monkeypatch.delenv("CHATHUB_API_KEY", raising=False)
