# chat-hub : projet de synthèse de la Phase 0

Un seul projet qui **remplace tous les exercices des Leçons 1 à 4**. À la fin tu auras :

- un serveur web (FastAPI) qui reçoit et stocke des messages de chat,
- un client en ligne de commande pour lui parler,
- des statistiques sur les messages,
- un pipeline asynchrone `chat -> cerveau -> voix` avec interruption (l'ossature d'un mini-Neuro),
- des tests, un dépôt Git propre, et (après la Leçon 5) un conteneur Docker.

## Comment travailler

Le dépôt contient la **structure**, des **docstrings qui expliquent quoi faire**, et des **tests déjà écrits**. Toi, tu remplaces chaque `raise NotImplementedError` (les `TODO`) par du vrai code.

1. **Un jalon à la fois**, dans l'ordre. Chaque jalon a ses tests :
   `python -m pytest tests/test_m1_models.py -x -q` (`-x` s'arrête au premier échec).
2. **Tu as le droit de tout chercher** : les leçons, la doc, moi. Le but est de construire, pas de réciter de mémoire. La mémorisation, c'est le rôle d'Anki, à côté.
3. **Git** : une branche par jalon (`git switch -c m1-store`), un commit par fonctionnalité qui marche, puis `git switch main` et `git merge m1-store`.
4. **Bloqué plus de 20 minutes sur un test ?** Lis le message d'erreur en entier (la dernière ligne dit souvent tout), relis la docstring, puis colle-moi l'erreur.
5. **En plus des tests fournis, écris 2 tests à toi par jalon** (c'est l'exercice de la Leçon 2).

## M0. Mise en route (≈ 1 h) : Leçon 1

- [ ] Copie ce dossier hors de l'archive, puis `git init` et premier commit
- [ ] `python -m venv .venv` puis active-le (le `.gitignore` est déjà fourni)
- [ ] `pip install "fastapi[standard]" pytest mypy`
- [ ] `pip freeze > requirements.txt`, puis commit
- [ ] Crée le dépôt GitHub, puis `git push -u origin main`
- [ ] Lance `python -m pytest` : **tout doit échouer**. C'est normal, rien n'est écrit encore.

## M1. Modèle et stockage (≈ 2 h) : Leçon 2

Fichiers : `chathub/models.py`, `chathub/store.py`. Tests : `tests/test_m1_*.py`

- [ ] `ChatMessage` en dataclass (champs et défauts expliqués dans le fichier)
- [ ] `MessageStore` : `add`, `get`, `list_messages`, `delete`
- [ ] Sauvegarde et rechargement JSON (`_save` / `_load`)
- [ ] Bonus : `python -m mypy chathub` sans erreur

Relire : Leçon 2 (dataclasses, `default_factory`, pytest, `tmp_path`).

## M2. Statistiques (≈ 1 h) : Leçon 1 (ancien `wordcount`)

Fichier : `chathub/stats.py`. Tests : `tests/test_m2_stats.py`

- [ ] `top_words` (indices dans la docstring : `re.findall`, `Counter.most_common`)
- [ ] `count_by_author`

## M3. L'API web (≈ 3 h) : Leçon 3

Fichier : `chathub/api.py`. Tests : `tests/test_m3_api.py`

- [ ] `/health`
- [ ] `POST /messages` (201) et `GET /messages?limit=`
- [ ] `GET /messages/{id}` (404 si absent) et `DELETE /messages/{id}`
- [ ] `/stats` (réutilise M2)
- [ ] Clé API : `X-API-Key` obligatoire pour POST et DELETE (`check_key`)
- [ ] Lance le vrai serveur : `uvicorn chathub.main:app --reload`, puis ouvre http://127.0.0.1:8000/docs et essaie tes routes dans le navigateur

Relire : Leçon 3 (FastAPI, `BaseModel`, `HTTPException`, `TestClient`).

## M4. Client en ligne de commande (≈ 2 h) : Leçons 1 et 3

Fichier : `chathub/cli.py`. Tests : `tests/test_m4_cli.py`

- [ ] `build_parser` avec sous-commandes `post`, `list`, `stats`
- [ ] `main` : appelle l'API avec `httpx`, affiche le résultat, retourne 0 ou 1
- [ ] Essaie pour de vrai (serveur lancé dans un autre terminal) :
  `python -m chathub.cli post vedal "salut le chat"` puis `python -m chathub.cli list`
- [ ] Stretch : sous-commande `pokemon NOM [NOM...]` qui affiche la taille de chaque Pokémon via `fetch_many` (M5)

Relire : Leçon 1 (`argparse`), Leçon 3 (`httpx`, `headers=`, `params=`).

## M5. Asynchrone (≈ 3 h) : Leçon 4

Fichiers : `chathub/pipeline.py`, `chathub/fetch.py`. Tests : `tests/test_m5_*.py`

- [ ] `fetch_many` : requêtes concurrentes, `Semaphore`, une erreur ne casse pas les autres
- [ ] `chat_producer`, `brain`, `speaker`, `run_pipeline` (files d'attente et sentinelle `None`)
- [ ] `speak` et `speak_with_interrupt` (`create_task`, `cancel`, `CancelledError`)
- [ ] **Casse-le exprès** : mets un `time.sleep(1)` dans `brain` et observe que tout gèle. C'est le bug à savoir repérer.

Relire : Leçon 4 (`gather`, `Semaphore`, `Queue`, annulation).

## M6. Docker (après la Leçon 5)

À faire quand on aura vu Docker : un `Dockerfile`, `docker build`, `docker run -p 8000:8000`, et un volume pour garder `messages.json`.

## Où sont passés les anciens exercices ?

| Ancien exercice | Dans ce projet |
|---|---|
| Leçon 1 : `wordcount`, `argparse`, Git, venv, `.gitignore`, `requirements.txt` | M2, M4, M0 |
| Leçon 1 : `newproject`, `tidy`, `gitstats` | Abandonnés (tu as fait la Leçon 1 : plus besoin) |
| Leçon 2 : dataclass `ChatMessage`, refactor en package, 6 tests pytest, `mypy` | M1 (+ tests fournis, 2 à toi) |
| Leçon 3 : `pokemon.py`, API chat-log, `client.py`, JSON, clé API | M4 stretch, M3, M4, M1, M3 |
| Leçon 4 : `timing.py` | Abandonné (optionnel : 10 minutes pour voir le gain de `gather`) |
| Leçon 4 : `fetch_all.py`, pipeline `chat -> brain -> speaker`, interruption | M5 |

## Définition de « terminé »

- [ ] `python -m pytest` : tout est vert
- [ ] Tu as lancé le serveur et le client à la main au moins une fois
- [ ] Le dépôt est sur GitHub, `.venv` et `messages.json` n'y sont pas, `requirements.txt` à jour
- [ ] Ce README contient un exemple d'utilisation (les commandes du client)
- [ ] Tu peux expliquer à voix haute pourquoi la logique est dans `store.py` et pas dans `api.py`
