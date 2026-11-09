# Exercice 1 : Carte de joueur
import time
from dataclasses import dataclass, field

@dataclass 
class Player:
    name:str
    level:int
    is_online:bool = field(default_factory=True)

neuro = Player(name='Neuro', level=10, is_online=True)
print(neuro)

# Exerciec 2 : Inventaire d'objets 

@dataclass 
class Inventory:
    owner: str
    items: list[str] = field(default_factory=[])

vedal_inventory = Inventory(owner="Vedal", items=["keyboards","mouse"])
neuro_inventory = Inventory(owner="Neuro", items=[])
print(vedal_inventory.items)
print(neuro_inventory.items)

# Exercice 3 : Message de twitch

@dataclass
class ChatMessage: 
    author: str 
    text: str 
    badges: list[str] = field(default_factory=list)
    is_mod: bool = False
    timestamp: float = field(default_factory=time.time)

vedal_message = ChatMessage("vedal", "Hello, Evil.", badges=["follower"], is_mod=True, timestamp=time.time())
neuro_message = ChatMessage("Neuro", "Hello", badges=["subscriber"])
mod_message = ChatMessage("Mod_1", "Hello !", ["subscriber"], is_mod=True)

def format_message(chat_message: ChatMessage)->str:
    return f"[{'MOD' if chat_message.is_mod else 'FOL'}] {chat_message.author} : {chat_message.text}"

print(format_message(vedal_message))
print(format_message(neuro_message))
print(format_message(mod_message))