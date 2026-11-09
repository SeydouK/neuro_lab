import argparse 
from finder.core import extension_finder, name_finder

parser = argparse.ArgumentParser(
    description="Find a file by extension."
)

parser.add_argument(
    "folder",
    help="Retourne les fichier avec une extension similaire."
)

parser.add_argument(
    "file_name",
    help="Le nom du fichier a trouver."
)

"""parser.add_argument(
    "extension", 
    help="Le nom de l'exentension des fichiers que tu veux trouver."
)"""

args = parser.parse_args()
#extension_finder(args.folder, args.extension)
name_finder(args.folder, args.file_name)