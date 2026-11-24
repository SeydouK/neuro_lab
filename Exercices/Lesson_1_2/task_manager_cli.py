"""Manage your tasks with style"""

import subprocess
from pathlib import Path 
from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from collections import Counter
from dataclasses import asdict, dataclass
import json

@dataclass
class Task(): 
    nom: str
    date: datetime 
    description: str
    statut: str

class TaskManager:
    def __init__(self, path: Optional[Path] = None) -> None:
        self.path = path 
        self.next_id = 1
        self.tasks = []


    def save_task(self, path: Path) -> None:
        path = path 
        filename = input("Entrez le nom du fichier:\n > ")
        file_path = next((file for file in path.iterdir() if file.stem == filename), None)

        if file_path is not None:
            file_path.write_text(self.tasks)
            print("Tache sauveguarder !")
        else:
            print("Ce fichier n'existe pas.")

    def add_task(self, path: Path) -> None:    
        filename = input("Entrez le nom du fichier:\n > ")
        if filename is not None:
            print("Ce fichier existe.")
            print("""Chaque tâche doit contenir :\n
                        - Un identifiant.\n
                        - Un nom.\n
                        - Une description.\n
                        - Une date de création.\n
                        - Un statut (`pending` ou `completed`)."""
                    )
            identifiant = self.next_id
            self.next_id += 1
            print(f"Identifiant : {identifiant}")
            date = datetime.now()
            print(f"Date : {date}")
            nom = input("Entrez le nom de la tache :\n > ")
            description = input("Entrez la description de la tache :\n > ")
            statut = "pending"

            task_model = Task(nom=nom, date=date, description=description, statut=statut)
            task_dict = {
                    'identifiant': identifiant, 
                    'details' : asdict(task_model)
            }
            self.tasks.append(task_dict)
            print(self.tasks)
        else:
            print("Ce fichier n'existe pas.")

    def main(self):
        while True:
            print("1. Ajouter une tâche\n")
            print("2. Afficher toutes les tâches\n")
            print("3. Marquer une tâche comme terminée\n")
            print("4. Supprimer une tâche\n")
            print("5. Compter les tâches par statut\n")
            print("6. Afficher les tâches les plus anciennes\n")
            print("7. Quitter\n")
            
            choix = int(input("> "))

            if self.path: 
                    cwd = Path(self.path)
                    print(f"CWD : {cwd}")
                    filename = input("Entrez le nom du fichier:\n > ")

            else: 
                    print("Aucun chemin donner\n")
                    print("Voulez vous utiliser le dossier dans lequel vous vous trouvez?\n")
                    choix = input("(Oui/Non) > ")
                    if choix.lower() == "oui": 
                        cwd = Path.cwd()
                        print(f"CWD : {cwd}")
                        if cwd.exists: 
                            self.add_task(cwd)
                        else :
                            print("Ce dossier n'existe pas.")

                    elif choix.lower() == "non":
                        return 1 
                    print("Ce choix n'existe pas.")
            
            if choix == 1:
                self.add_task(cwd, filename)

            elif choix == 2:
                print("Liste des taches: \n")
                for task in self.tasks: 
                    print(task)

            elif choix == 3:
                task_name = input("Entrez le nom :\n > ")
                task_pending = next((task['details'] for task in self.tasks if task['details']['nom']==task_name), None)
                
                if task_pending == None: 
                    print("Cette tache n'existe pas.")

                if task_pending['statut'] != "completed":
                    task_pending['statut'] = 'completed'
                    print("La tache a ete completee !")
                else :
                    print("Cette tache a deja ete completee.")

            elif choix == 4:
                print("Supprimer une tache: \n")
                id_task = int(input("Entrez le numero de la tache a supprimee:\n > "))
                for task in self.tasks: 
                    if task['id'] == id_task:
                        self.tasks.remove(task)
                    else:
                        print("Cet ID n'existe pas.")
            
            elif choix == 5: 
                count_by_statut = Counter(task['details']['statut'] for task in self.tasks)
                print(count_by_statut)

            elif choix == 6: 
                print(sorted((task['details']['date'] for task in self.tasks), reverse=True))

            elif choix == 8: 
                print("Aurevoir !")
                break
            else:
                print("Ce choix n'existe pas.")
if __name__ == "__main__": 
    manager = TaskManager()
    manager.main()

