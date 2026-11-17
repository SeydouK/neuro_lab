"""Modèle de données : un message du chat (Leçon 2 : dataclasses + type hints)."""

from datetime import datetime
from dataclasses import dataclass, field


def now_iso() -> str:
    """Date et heure actuelles en texte ISO, ex. '2026-11-13T14:30:00'."""
    return datetime.now().isoformat(timespec="seconds")


# TODO (M1) : transforme cette classe en dataclass avec ces champs, dans cet ordre :
#   author: str
#   text: str
#   id: int = 0
#   created_at: str   -> par défaut now_iso() calculé à la création du message
#                        (indice : field(default_factory=...), comme pour une liste)
@dataclass
class ChatMessage:
    author: str
    text: str 
    id: int = 0
    created_at: str = field(default_factory=now_iso)
