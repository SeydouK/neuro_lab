from pathlib import Path 
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

def organize_folder(folder, dry_run=False):
    folder = Path(folder).resolve()

    if not folder.is_dir():
        print(f"{folder} doesnt exist.")
        return 
    
    for file in folder.iterdir():
        if not file.is_file():
            continue 

        category = category_for(file)
        organize(folder, file, category)


def category_for(file):
    return CATEGORIES.get(file.suffix.lower(), "other")


def organize(folder, file, category, dry_run=False):
    destination_folder = folder / category
    destination = destination_folder / file.name

    if destination.exists():
        print(f"Skipping: {file.name} (destination exists)")
        return

    if dry_run:
        print(f"Would move: {file.name} -> {category}/{file.name}")
        return

    destination_folder.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file), str(destination))
    print(f"Moved: {file.name} -> {category}/{file.name}")