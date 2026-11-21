"""Créer un système permettant d'enregistrer des Pokémon favoris."""

import sys
import httpx

print(20*"=" + " POKEMON FAVORIS " + "="*20)

def main():
    url = "https://pokeapi.co/api/v2"
    my_pokemons = []   
    while True: 
        print("1- Entrez un nouveau Pokemon \n")
        print("2- Listez vos Pokemon favoris \n")
        print("3- Supprimez un Pokemon\n")
        print("4- Quitter\n")
        choix = int(input("> "))

        if choix == 1: 
            try:
                client = httpx.Client(
                    base_url = url,
                    timeout=10
                )
                params = {
                    "offset":0,
                    "limit":100
                }
                response = client.get(
                    "/pokemon",
                    params = params
                )
                print(response)
                if response.is_error:
                    print(f"HTTP error: {response.status_code}", file=sys.stderr)
                    return 1

                pokemons = response.json()
                pokemons = [pokemon['name'] for pokemon in pokemons['results']]
                
                print(f"Liste de 100 pokemons disponible: \n")
                print(pokemons)

                print("Vos pokemons: ")
                print(my_pokemons)

                pokemon = input("Entrez un nouveau pokemon: ")
                my_pokemons.append(pokemon)

                if pokemon in pokemons: 
                    print(f"{pokemon} ajouter!")
                else:
                    print("Ce pokemon n'existe pas.")            
            except httpx.RequestError as e:
                print("Impossible de joindre le destinateur pour l'instant. \n")
                return 1

        elif choix == 2: 
            print("Voici votre liste de pokemon favoris: ")
            print(my_pokemons)
        
        elif choix == 3: 
            while True:
                print("1- Supprimer un pokemon \n")
                print("2- Vider la liste\n")
                print("3- Quitter\n")
                choix = int(input("> "))

                if choix == 1: 
                    pokemon = input("Entrez le nom du pokemon: ")
                    if pokemon in my_pokemons:
                        my_pokemons.remove(pokemon)
                        print(f"{pokemon} a ete supprimer.")
                        print(f"Votre nouvelle liste : {my_pokemons}")
                    else: 
                        print("Ce pokemon n'existe pas dans votre lsite.")
                elif choix == 2: 
                    choix = input("Etes vous sur? (oui/non)\n> ")
                    if choix == "oui":
                        if len(my_pokemons) != 0:
                            my_pokemons = []
                            print("Liste vider")
                        else: 
                            print("Liste deja vide")
                    elif choix == "non": 
                        continue 
                    else: 
                        print("Ce choix n'est pas disponible.")
                elif choix == 3: 
                    print("Aurevoir!")
                    break 
        elif choix == 4:
            print("Aurevoir !")
            break 
        
        else: 
            print("Ce choix n'existe pas.")


if __name__ == "__main__":
    main()
    
