"""L'API web (Leçon 3 : FastAPI). Elle appelle MessageStore et stats, elle ne contient pas de logique métier."""

from dataclasses import asdict
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
from chathub.store import MessageStore
from chathub.stats import count_by_author, top_words 


class MessageIn(BaseModel):
    """Corps attendu pour POST /messages. FastAPI renvoie 422 si un champ manque."""

    author: str
    text: str


def create_app(store: Optional[MessageStore] = None, api_key: Optional[str] = None) -> FastAPI:
    """Fabrique l'application. On passe le store en paramètre pour pouvoir le remplacer dans les tests.

    - api_key = None : aucune protection.
    - api_key = "secret" : POST et DELETE exigent l'en-tête  X-API-Key: secret  (sinon 401).
      Les GET restent publics.
    """
    the_store = store if store is not None else MessageStore()
    app = FastAPI(title="chat-hub")

    def check_key(x_api_key: Optional[str] = None) -> None:
        """Lève HTTPException(401) si api_key est défini et que x_api_key est différent."""
        # TODO (M3)
        if api_key is not None and api_key != x_api_key:
            raise HTTPException(
                status_code = 401, 
                detail="Cette clée n'est pas permise.")


    @app.get("/health")
    def health():
        """Retourne {"status": "ok"}"""
        # TODO (M3)
        return {'status':'ok'}

    @app.post("/messages", status_code=201)
    def add_message(msg: MessageIn, x_api_key: Optional[str] = Header(default=None)):
        """Vérifie la clé, ajoute le message au store, retourne le message sous forme de dict (asdict)."""
        # TODO (M3)
        check_key(x_api_key=x_api_key)
        return asdict(the_store.add(author=msg.author, text=msg.text))


    @app.get("/messages")
    def list_messages(limit:Optional[int] = None):
        """Retourne la liste des messages (dicts). ?limit=2 -> les 2 derniers."""
        messages = []
        for message in the_store.list_messages(limit):
            messages.append(asdict(message))
        return messages

    @app.get("/messages/{msg_id}")
    def get_message(msg_id: int):
        """Retourne le message en dict, ou HTTPException 404 ("Message introuvable")."""
        # TODO (M3)
        message = the_store.get(msg_id)
        if message:
            return asdict(message)
        raise HTTPException(status_code=404, detail="Message introuvable")

    @app.delete("/messages/{msg_id}")
    def delete_message(msg_id: int, x_api_key: Optional[str] = Header(default=None)):
        """Vérifie la clé, supprime le message (404 s'il n'existe pas), retourne {"deleted": msg_id}."""
        # TODO (M3)
        check_key(x_api_key)
        try:
            the_store.delete(msg_id)
            return {"deleted": msg_id}
        except KeyError as e: 
            raise HTTPException(status_code=404, detail=str(e))


    @app.get("/stats")
    def stats(top: int = 5):
        """Retourne {"total": ..., "top_words": [[mot, n], ...], "by_author": {auteur: n}}
        en utilisant chathub.stats."""
        # TODO (M3)
        liste_messages = the_store.list_messages()
        count_stats = {
            "total":len(liste_messages),
            "top_words":top_words(liste_messages, top), 
            "by_author":count_by_author(liste_messages)
        } 
        return count_stats

    return app
