from collections import defaultdict
from pathlib import Path 

print("==== EXPLORATEUR DE FICHIERS ====")

folder_name = input("Entrez le nom du dossier : ")

cwd = Path(folder_name).resolve()

extensions = defaultdict(int)

def create_file(cwd, filename):
    file_path = Path(f"{cwd}\{filename}.txt").resolve()
    if file_path.exists() and file_path.is_file():
        print("Ce fichier existe déjà.\n")
        print("1 - Lire le contenu du fichier\n")
        print("2 - Supprimer le fichier\n")
        print("3 - Quitter\n")
        choice = int(input("> "))

        if choice == 1: 
            content = file_path.read_text()
            print(content)
        elif choice == 2: 
            file_path.unlink()
            print("Fichier supprimé !")
        elif choice == 3:
            print("Au revoir !")
        else: 
            print("Cette option n'existe pas.")
    else: 
        file_path.touch()
        print("Fichier créé !")
        print("1 - Voulez-vous écrire dans ce fichier ?\n")
        print("2 - Quitter\n")
        choice = int(input("> "))

        if choice == 1:
            print("Entrez le texte : ")
            content = input("> ")
            file_path.write_text(content)
            print("TERMINÉ !")
        elif choice == 2:
            print("Au revoir !")
        else: 
            print("Cette option n'existe pas.")


if cwd.exists():
    print("Ce dossier existe.")
    for file in cwd.iterdir():
        print(f"Nom du fichier : {file.stem}: \n")
        print(f"\t Extension : {file.suffix}\n")
        print(f"\t Chemin : {cwd}\n")

        if extensions[file.suffix] in extensions.keys():
            extensions[file.suffix] = 1;
        else:
            extensions[file.suffix] += 1

    print(f"Nombre de fichiers par extension :\n \t {extensions}")

    print("Créons un fichier !")
    print("Entrez un nom : ")
    file_name = input("> ")
    create_file(cwd, file_name)
else: 
    print("Ce dossier n'existe pas.")
    print("Voulez-vous le créer ? ")
    print("1 - Oui")
    print("2 - Non")
    choice = int(input("> "))
    print("\n")

    if choice == 1: 
        cwd.mkdir()
        print(f"Le dossier existe à l'emplacement : {cwd}")

        print("Entrez le nom du fichier que vous voulez créer : ")
        name_file = input("> ")
        create_file(cwd, name_file)
    elif choice == 2:
        print("D'accord, au revoir !")
    else: 
        print("Cette option n'existe pas.")