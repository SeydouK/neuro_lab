"""Point d'entrée du serveur (déjà écrit). Lance-le avec :

    uvicorn chathub.main:app --reload

Variable d'environnement optionnelle : CHATHUB_API_KEY (active la protection par clé).
"""

import os
from pathlib import Path

from chathub.api import create_app
from chathub.store import MessageStore

app = create_app(MessageStore(Path("messages.json")), api_key=os.environ.get("CHATHUB_API_KEY"))
