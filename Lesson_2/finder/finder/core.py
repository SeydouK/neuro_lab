from pathlib import Path 


def extension_finder(folder, extension):
    folder = Path(folder).resolve()

    if not folder.is_dir():
        print("This folder doesn't exist.")

    liste_fichier = []

    for file in folder.iterdir():
        if not file.is_file():
            continue
        
        if file.suffix.lower() == extension.lower():
            print(file.name) 
    
    if len(liste_fichier) == 0:
        print(f"Il n'existe aucun fichier avec l'extension {extension} dans le dossier {folder}");
    else:
        print(f"Nous avons trouver {len(liste_fichier)} fichiers correspondants: ")
        for fichier in liste_fichier:
            print(fichier)

def name_finder(folder, file_name):
    folder = Path(folder).resolve()
        
    trouver = False 

    for file in folder.iterdir():
        if not file.is_file():
            continue 
        
        if file.name.strip() == file_name.strip():
            print(f"Fichier trouver : {file.name}.")
            trouver = True
    if trouver == False: 
        print("Ce fichier n'existe pas.")


