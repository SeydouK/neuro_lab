"""Stockage des messages : logique PURE, sans FastAPI ni print (Leçon 2 : séparer logique et I/O)."""

import datetime
from inspect import indentsize
from pathlib import Path
from sqlite3.dbapi2 import Timestamp

from chathub.models import ChatMessage

from dataclasses import asdict

import json

class MessageStore:
    """Garde les messages en mémoire, et dans un fichier JSON si un chemin est donné."""

    def __init__(self, path: Path | None = None) -> None:
        """Prépare le stockage.

        - self.path = path
        - une liste de messages (vide au départ) et un compteur d'id qui commence à 1
        - si path existe déjà sur le disque, recharge son contenu (voir _load)
        """
        self.path = path
        self.messages = []
        self.next_id = 1
        if self.path is not None :
            self.path = path.resolve()
            if path.exists() and path.is_file():
                self._load()


    def add(self, author: str, text: str) -> ChatMessage:
        """Crée un message avec le prochain id (1, 2, 3...), le stocke, sauvegarde, et le retourne."""
        chatMessage = ChatMessage(id=self.next_id ,author=author, text=text)
        self.next_id += 1
        self.messages.append(chatMessage)
        self._save()
        return chatMessage

    def get(self, msg_id: int) -> ChatMessage:
        """Retourne le message ayant cet id. Lève KeyError s'il n'existe pas."""
        for i in self.messages: 
                if i.id == msg_id:
                    return i
        raise KeyError("Ce message n'existe pas.")

    def list_messages(self, limit: int | None = None) -> list[ChatMessage]:
        """Sans limit : tous les messages, dans l'ordre.
        Avec limit : seulement les `limit` DERNIERS messages. limit=0 -> liste vide.
        (Attention : liste[-0:] renvoie tout !)"""
        if limit != None: 
            if len(self.messages) > 0 and limit > 0:
                return self.messages[-limit:]
            else:
                return []
        else:
            return self.messages
                

    def delete(self, msg_id: int) -> None:
        """Supprime le message. Lève KeyError s'il n'existe pas. Les ids supprimés ne sont jamais réutilisés."""
        for index, i in enumerate(self.messages): 
            if i.id == msg_id:
                del self.messages[index]
                self._save()
                break
        else:
            raise KeyError("Ce message n'existe pas.")

    def _save(self) -> None:
        """Si self.path est None : ne fait rien (aucun fichier créé).
        Sinon écrit un JSON : {"next_id": ..., "messages": [ {author, text, id, created_at}, ... ]}
        Indices : dataclasses.asdict, json.dumps(..., indent=2), Path.write_text."""
        if self.path != None: 
            if self.path == None:
                return 

            data = {
                'next_id': self.next_id, 
                'messages': [asdict[message] for message in self.messages]
            }
            self.path.write_text(json.dumps(data, indent=2))


    def _load(self) -> None:
        """Relit le fichier JSON écrit par _save et remplit la liste de messages et le compteur.
        Indices : Path.read_text, json.loads, ChatMessage(**dictionnaire)."""
        data = json.loads(self.path.read_text())
        self.next_id = data['next_id']
        self.messages = [
            ChatMessage(**message)
            for message in data['messages']
        ]

