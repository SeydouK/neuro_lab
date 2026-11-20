"""Client en ligne de commande (Leçon 1 : argparse, Leçon 3 : httpx).

Exemples une fois fini :
    python -m chathub.cli post vedal "salut le chat"
    python -m chathub.cli list --limit 5
    python -m chathub.cli stats --top 3
"""

import argparse
import os
import sys

from typing import Optional 

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
    parser = argparse.ArgumentParser(
      description=""
    )

    parser.add_argument("--url", default="http://127.0.0.1:8000")
    parser.add_argument("--api-key", default=os.getenv("CHATHUB_API_KEY"))

    subparsers = parser.add_subparsers(dest="command", required=True)

    post_parser = subparsers.add_parser("post", help="Envoyer un message")
    post_parser.add_argument("author")
    post_parser.add_argument("text")

    list_parser = subparsers.add_parser("list", help="Afficher les messages")
    list_parser.add_argument("--limit", type=int)
    
    stats_parser = subparsers.add_parser("stats", help="Afficher les statistiques")
    stats_parser.add_argument("--top", type=int, default=5)

    return parser
  


def main(argv: Optional[list[str]] = None, client: Optional[httpx.Client] = None) -> int:
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
    parser = build_parser()
    args = parser.parse_args(argv)
    headers = {}

    if client is None: 
      client = httpx.Client(
        base_url=args.url,
        timeout=10
      )
    try:
      headers = {}

      if args.api_key is not None:
        headers['X-API-Key'] = args.api_key 

      if args.command == "post": 
        body = {
          "author": args.author, 
          "text": args.text
        }

        response = client.post(
            "/messages", 
            json=body, 
            headers=headers
          )

        if response.is_error: 
          print(f"HTTP error: {response.status_code}", file=sys.stderr)
          return 1 

        data = response.json()
        print(f"[{data['id']}] {data['author']}: {data['text']}")

      elif args.command == "list":
        params = {}

        if args.limit is not None: 
          params["limit"] = args.limit

        response = client.get(
          "/messages",
          params=params, 
          headers=headers
        )      
        if response.is_error: 
          print(f"HTTP error: {response.status_code}", file=sys.stderr)
          return 1

        data = response.json()

        for message in data: 
          print(f"[{message['id']}] {message['author']}: {message['text']}")

      elif args.command == "stats":
        params = {}

        if args.top is not None: 
          params['top'] = args.top 
        
        response = client.get(
          "/stats",
          params = params,
          headers = headers
        )

        if response.is_error: 
          print(f"HTTP error: {response.status_code}", file=sys.stderr)
          return 1

        data = response.json()

        print(f"Total : {data['total']}")

        print("Top words:")
        for word, count in data["top_words"]:
          print(f"    {word}: {count}")

        print("By Author:")
        for author, count in data["by_author"].items():
          print(f"    {author}: {count}")

    except httpx.RequestError as e: 
      print(f"Server unreachable: {e}", file=sys.stderr)
      return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
