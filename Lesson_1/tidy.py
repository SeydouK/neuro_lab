
from pathlib import Path
import argparse
import shutil

CATEGORIES = {
    ".pdf": "pdf",
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
    ".webp": "images",
    ".py": "code",
    ".js": "code",
    ".html": "code",
    ".css": "code",
}


def organize(folder, dry_run=False):
    folder = Path(folder).resolve()

    if not folder.is_dir():
        print(f"Error: folder does not exist: {folder}")
        return

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = CATEGORIES.get(file.suffix.lower(), "other")
        destination_folder = folder / category
        destination = destination_folder / file.name

        # Never overwrite an existing file.
        if destination.exists():
            print(f"Skipping: {file.name} (destination exists)")
            continue

        if dry_run:
            print(f"Would move: {file.name} -> {category}/{file.name}")
        else:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {category}/{file.name}")


def main():
    parser = argparse.ArgumentParser(
        description="Organize files by extension."
    )
    parser.add_argument(
        "folder",
        help="Folder to organize"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()
    organize(args.folder, args.dry_run)


if __name__ == "__main__":
    main()
