import argparse
from tidy.core import organize_folder

parser = argparse.ArgumentParser(
    description="Organize folders by extension."
)
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Previez changes without moving files"
)
parser.add_argument(
    "folder",
    help="Folder to organize"
)

args = parser.parse_args()

organize_folder(args.folder, args.dry_run)