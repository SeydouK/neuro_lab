"""Statistiques sur les messages : fonctions pures (ancien exercice wordcount, Leçon 1)."""

from .models import ChatMessage
import re 
from collections import Counter

def top_words(messages: list[ChatMessage], n: int = 5) -> list[tuple[str, int]]:
    """Les n mots les plus fréquents dans le texte de tous les messages, du plus au moins fréquent.

    - insensible à la casse : "Hello" et "hello" comptent pour le même mot
    - la ponctuation est ignorée : "world!" -> "world"
    Retour : [("hello", 3), ("world", 2)]
    Indices : re.findall(r"\\w+", texte.lower()), collections.Counter, .most_common(n)
    """
    # TODO (M2)
    words: list[str] = []

    for message in messages: 
        words.extend(re.findall(r'\w+', message.text.lower()))

    return Counter(words).most_common(n)

def count_by_author(messages: list[ChatMessage]) -> dict[str, int]:
    """Nombre de messages par auteur. Retour : {"vedal": 2, "neuro": 1}"""
    # TODO (M2)
    auteurs: list[str] = []
    for message in messages: 
        auteurs.extend(re.findall(r'\w+', message.author.lower()))

    return dict(Counter(auteurs))
