# Exercice 1 : Calculateur de points 

def add_points(points:int, bonus:int=0)->int:
    return points + bonus

print(add_points(100,50))
print(add_points(100))

# Exercice 2 : Find users 

def find_user(uid:int)->str:
    users: dict[int, str] = {
        1: "vedal",
        2: "neuro",
        3: "evil"
    }

    return users.get(uid)

print(find_user(1))
print(find_user(99))


# Exercice 3 : statistiques 
messages: dict[str, list[str]] = {
        "vedal": ["hello", "hi"],
        "neuro": ["bonjour", "salut", "hey"],
        "evil": ["yo"]
    }
def count_messages(messages:dict, name:str)->int: 
    return len(messages.get(name))

print(count_messages(messages, "vedal"))
print(count_messages(messages, "neuro"))

