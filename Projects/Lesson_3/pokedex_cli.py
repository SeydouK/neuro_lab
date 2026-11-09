
import httpx

print("Bienvenue dans le Pokédex - CLI")
pokemon = input("Entrez le nom du pokemon :")

while True:

    print("===== MENU =====\n")
    print("1 - Afficher les statistiques\n")
    print("2 - Afficher ses capacités\n")
    print("3 - Son poids et sa taille\n")
    print("4 - Changer le nom du pokemon\n")
    print("5 - Quitter\n")

    try:
        choice = int(input("> "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if choice == 5:
        print("Au revoir !")
        break

    elif choice == 4:
        pokemon = input("Entrez le nom du pokemon :")
        continue

    elif choice in (1, 2, 3):

        try:
            r = httpx.get(
                f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}",
                timeout=10
            )
            r.raise_for_status()
            data = r.json()

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                print("Erreur : Pokémon introuvable !")
            else:
                print(f"Erreur HTTP : {e.response.status_code}")
            continue

        except httpx.RequestError as e:
            print(f"Erreur de connexion : {e}")
            continue

        if choice == 1:
            print(f"Name: {data['name']}\n")

            for stat in data['stats']:
                print(
                    f"{stat['stat']['name']}: "
                    f"{stat['base_stat']}"
                )

        elif choice == 2:
            for ability in data['abilities']:
                print(f"Passive : {ability['ability']['name']}")

            for move in data['moves']:
                print(f"Move : {move['move']['name']}")

        elif choice == 3:
            print(f"Height : {data['height']}")
            print(f"Weight : {data['weight']}")

    else:
        print("Ce choix n'existe pas.")
