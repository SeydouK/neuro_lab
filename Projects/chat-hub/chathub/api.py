"""L'API web (Leçon 3 : FastAPI). Elle appelle MessageStore et stats, elle ne contient pas de logique métier."""

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from chathub.store import MessageStore


class MessageIn(BaseModel):
    """Corps attendu pour POST /messages. FastAPI renvoie 422 si un champ manque."""

    author: str
    text: str


def create_app(store: MessageStore | None = None, api_key: str | None = None) -> FastAPI:
    """Fabrique l'application. On passe le store en paramètre pour pouvoir le remplacer dans les tests.

    - api_key = None : aucune protection.
    - api_key = "secret" : POST et DELETE exigent l'en-tête  X-API-Key: secret  (sinon 401).
      Les GET restent publics.
    """
    the_store = store if store is not None else MessageStore()
    app = FastAPI(title="chat-hub")

    def check_key(x_api_key: str | None) -> None:
        """Lève HTTPException(401) si api_key est défini et que x_api_key est différent."""
        # TODO (M3)
        raise NotImplementedError

    @app.get("/health")
    def health():
        """Retourne {"status": "ok"}"""
        # TODO (M3)
        raise NotImplementedError

    @app.post("/messages", status_code=201)
    def add_message(msg: MessageIn, x_api_key: str | None = Header(default=None)):
        """Vérifie la clé, ajoute le message au store, retourne le message sous forme de dict (asdict)."""
        # TODO (M3)
        raise NotImplementedError

    @app.get("/messages")
    def list_messages(limit: int | None = None):
        """Retourne la liste des messages (dicts). ?limit=2 -> les 2 derniers."""
        # TODO (M3)
        raise NotImplementedError

    @app.get("/messages/{msg_id}")
    def get_message(msg_id: int):
        """Retourne le message en dict, ou HTTPException 404 ("Message introuvable")."""
        # TODO (M3)
        raise NotImplementedError

    @app.delete("/messages/{msg_id}")
    def delete_message(msg_id: int, x_api_key: str | None = Header(default=None)):
        """Vérifie la clé, supprime le message (404 s'il n'existe pas), retourne {"deleted": msg_id}."""
        # TODO (M3)
        raise NotImplementedError

    @app.get("/stats")
    def stats(top: int = 5):
        """Retourne {"total": ..., "top_words": [[mot, n], ...], "by_author": {auteur: n}}
        en utilisant chathub.stats."""
        # TODO (M3)
        raise NotImplementedError

    return app
