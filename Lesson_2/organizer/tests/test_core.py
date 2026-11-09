import pytest 
from organizer.core import organize 

def test_organiser():
    result = organize(
        r"C:\Users\skabo\OneDrive\Bureau\Books\Politiques\Les bases"
    )

    assert result == (
        "engels-principes-du-communisme is a .pdf file.\n"
        "marx_karl_-_manifeste_du_parti_communiste is a .pdf file.\n"
        "Socialisme utopique et socialisme scientifique is a .pdf file."
    )

import argparse 
parser = argparse.ArgumentParser(
    Description="Organize files in a directory"
)

import subprocess 

oneline =subprocess.run("git log --oneline", shell=True, text=True, capture_output=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")
print(oneline.stdout)

oneline_second = subprocess.run(["git", "log", "--format=%h %s"], capture_output=True, text=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")
print(oneline_second.stdout)