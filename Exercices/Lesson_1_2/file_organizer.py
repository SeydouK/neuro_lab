from pathlib import Path 
import shutil

print("==== File Organizer ====")

cwd = input("Entrer le chemin du dossier a classer: ")
cwd = Path(cwd).resolve()

extensions = {}

if not cwd.exists():
    print("Ce dossier n'existe pas.")
else: 
    for file in cwd.iterdir():
        extensions[file.suffix] = extensions.get(file.suffix, 1) + 1
    
    for extension in extensions.keys():
        print(f"Nous avons {extensions[extension]} fichiers avec l'extension {extension}\n")

    print("==== Création des dossiers ====\n")
    for extension in extensions.keys():
        path = cwd/extension 
        path.mkdir(exist_ok=True)
        print(f"Dossier {path} créer!\n")

    for file in cwd.iterdir():
        print()
        source = cwd/file
        print("source: ", source)
        destination = cwd/file.suffix
        print("destination", destination)
        print()
        try:
            shutil.move(str(source), str(destination))
            print(f"{file} deplacé dans le dossier {extension}.")
        except shutil.Error as e:
            print("Erreur: ", e)

        