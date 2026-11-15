"""Client en ligne de commande (Leçon 1 : argparse, Leçon 3 : httpx).

Exemples une fois fini :
    python -m chathub.cli post vedal "salut le chat"
    python -m chathub.cli list --limit 5
    python -m chathub.cli stats --top 3
"""

import argparse
import os
import sys

import httpx


def build_parser() -> argparse.ArgumentParser:
    """Construit le parseur d'arguments.

    Options globales :
      --url       (défaut "http://127.0.0.1:8000")
      --api-key   (défaut : variable d'environnement CHATHUB_API_KEY, ou None)
    Sous-commandes (indice : parser.add_subparsers(dest="command", required=True)) :
      post AUTHOR TEXT       envoyer un message
      list [--limit N]       afficher les messages (N est un int)
      stats [--top N]        afficher les statistiques (défaut 5)
    """
    # TODO (M4)
    raise NotImplementedError


def main(argv: list[str] | None = None, client: httpx.Client | None = None) -> int:
    """Exécute une commande et retourne le code de sortie (0 = OK, 1 = erreur).

    - argv=None -> argparse lit sys.argv. Dans les tests on passe une liste.
    - client=None -> créer httpx.Client(base_url=args.url, timeout=10). Dans les tests on injecte un client.
    - si une clé API est donnée, l'envoyer dans l'en-tête X-API-Key
    - post  : POST /messages    puis afficher  [id] auteur: texte
    - list  : GET  /messages    (params limit si donné), une ligne  [id] auteur: texte  par message
    - stats : GET  /stats       afficher le total, puis chaque mot du top avec son nombre, puis les auteurs
    - erreur HTTP : si r.is_error est True (statut 4xx/5xx), afficher le code sur stderr et retourner 1
      (on n'utilise pas raise_for_status ici : dans les tests le client injecté vient de FastAPI,
      et ses exceptions ne sont pas celles de httpx)
    - serveur injoignable (except httpx.RequestError) : afficher un message sur stderr, retourner 1
    """
    # TODO (M4)
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())
