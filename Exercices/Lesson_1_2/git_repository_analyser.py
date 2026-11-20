import subprocess
from pathlib import Path
from pydantic_core.core_schema import DatetimeSchema
from datetime import datetime, timezone
from collections import Counter 

print(4*"=","cGIT REPOSITORY ANALYSERc",4*"=")
print()

print("MENU\n")
print("1 - Récupérer tous les commits \n")
print("2 - Afficher les auteurs \n")
print("3 - Compter le nombre de commits par auteur \n")
print("4 - Afficher les dates des commits \n")
print("5 - Identifier le jour où il y a eu le plus de commits \n")
print("6 - Afficher les dix derniers commits \n")
choice = int(input(" > "))

cwd = Path.cwd()
print(cwd)

is_repo_git = (cwd/".git").exists()

if is_repo_git:
    if choice == 1: 
        commits = subprocess.run(["git", "log", "--oneline"], capture_output=True, text=True, cwd=cwd, check=True).stdout
        print(commits)

    elif choice == 2:
        auteurs = subprocess.run(["git", "log", "--format=%an"], capture_output=True, cwd=cwd, check=True).stdout
        set_auteurs = set(auteurs.splitlines())
        print(f"Les auteurs sont: {set_auteurs}")

    elif choice == 3: 
        auteurs = subprocess.run(["git", "log", "--format=%an"], capture_output=True, cwd=cwd, text=True, check=True).stdout
        a_commits = subprocess.run(["git", "log", "--format=%an %s"], capture_output=True, cwd=cwd, text=True, check=True).stdout
        commits_per_authors = {}

        for auteur in auteurs.splitlines():
            for a_commit in a_commits.splitlines():
                if auteur in a_commit:
                    commits_per_authors[auteur] = commits_per_authors.get(auteur, 0) + 1

        print(commits_per_authors)

    elif choice == 4:
        dates = subprocess.run(["git", "log", "--format=%ct"], capture_output=True, cwd=cwd, text=True, check=True).stdout 

        for date in dates.splitlines():
            date = datetime.fromtimestamp(int(date), tz=timezone.utc)
            print(date)
            
    elif choice == 5: 
        try :
            commits = subprocess.run(
                ["git", "log", "--format=%ad", "--date=format:'%A %m %y'"],
                capture_output=True,
                cwd=cwd,
                text=True,
                check=True
            ).stdout        

            dates = Counter(commits.splitlines())
            print(f"Le jour avec le plus de commits : {dates.most_common(1)}")

        except subprocess.CalledProcessError as e: 
            print("Return code:", e.returncode)
            print("Git error:", e.stderr)
            print("Git ouput:", e.stdout)

    elif choice == 6: 
        commits = subprocess.run(["git", "log", "--format=%s"], capture_output=True, cwd=cwd, check=True).stdout.splitlines()

        print("Les cinq derniers commits: \n")
        
        for commit in commits[-10:]: 
            print(commit)
else:
    print("Aucun repository n'existe dans ce dossier.")


