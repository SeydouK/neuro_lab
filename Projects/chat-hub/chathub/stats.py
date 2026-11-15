"""Statistiques sur les messages : fonctions pures (ancien exercice wordcount, Leçon 1)."""

from chathub.models import ChatMessage


def top_words(messages: list[ChatMessage], n: int = 5) -> list[tuple[str, int]]:
    """Les n mots les plus fréquents dans le texte de tous les messages, du plus au moins fréquent.

    - insensible à la casse : "Hello" et "hello" comptent pour le même mot
    - la ponctuation est ignorée : "world!" -> "world"
    Retour : [("hello", 3), ("world", 2)]
    Indices : re.findall(r"\\w+", texte.lower()), collections.Counter, .most_common(n)
    """
    # TODO (M2)
    raise NotImplementedError


def count_by_author(messages: list[ChatMessage]) -> dict[str, int]:
    """Nombre de messages par auteur. Retour : {"vedal": 2, "neuro": 1}"""
    # TODO (M2)
    raise NotImplementedError
