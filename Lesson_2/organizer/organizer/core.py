from pathlib import Path

def organize(path):
    cwd = Path(path).resolve()

    if not cwd.is_dir():
        return "Ce dossier n'existe pas."
    
    files = []

    for file in cwd.iterdir():
        if file.is_file():
            files.append(f"{file.stem} is a {file.suffix} file.")

    if not files:
        return "There is no file in this folder."

    return "\n".join(files)

