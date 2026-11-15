"""Stockage des messages : logique PURE, sans FastAPI ni print (Leçon 2 : séparer logique et I/O)."""

from pathlib import Path

from chathub.models import ChatMessage


class MessageStore:
    """Garde les messages en mémoire, et dans un fichier JSON si un chemin est donné."""

    def __init__(self, path: Path | None = None) -> None:
        """Prépare le stockage.

        - self.path = path
        - une liste de messages (vide au départ) et un compteur d'id qui commence à 1
        - si path existe déjà sur le disque, recharge son contenu (voir _load)
        """
        # TODO (M1)
        raise NotImplementedError

    def add(self, author: str, text: str) -> ChatMessage:
        """Crée un message avec le prochain id (1, 2, 3...), le stocke, sauvegarde, et le retourne."""
        # TODO (M1)
        raise NotImplementedError

    def get(self, msg_id: int) -> ChatMessage:
        """Retourne le message ayant cet id. Lève KeyError s'il n'existe pas."""
        # TODO (M1)
        raise NotImplementedError

    def list_messages(self, limit: int | None = None) -> list[ChatMessage]:
        """Sans limit : tous les messages, dans l'ordre.
        Avec limit : seulement les `limit` DERNIERS messages. limit=0 -> liste vide.
        (Attention : liste[-0:] renvoie tout !)"""
        # TODO (M1)
        raise NotImplementedError

    def delete(self, msg_id: int) -> None:
        """Supprime le message. Lève KeyError s'il n'existe pas. Les ids supprimés ne sont jamais réutilisés."""
        # TODO (M1)
        raise NotImplementedError

    def _save(self) -> None:
        """Si self.path est None : ne fait rien (aucun fichier créé).
        Sinon écrit un JSON : {"next_id": ..., "messages": [ {author, text, id, created_at}, ... ]}
        Indices : dataclasses.asdict, json.dumps(..., indent=2), Path.write_text."""
        # TODO (M1)
        raise NotImplementedError

    def _load(self) -> None:
        """Relit le fichier JSON écrit par _save et remplit la liste de messages et le compteur.
        Indices : Path.read_text, json.loads, ChatMessage(**dictionnaire)."""
        # TODO (M1)
        raise NotImplementedError
