from collections import defaultdict 
from datetime import datetime, timezone
from gc import freeze
import subprocess

dicto = {
    "a":12,
    "b":124,
    "g":12
}

sorted(dicto.items(), key=lambda kv:kv[1], reverse=True)
sorted(dicto.items(), key=lambda k:k[0], reverse=True)

print(list(dicto.items())[1][1])
print(dicto.get("a"))
print(sorted(dicto.items(), key=lambda kv:kv[1], reverse=True))


fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
d = defaultdict(int)

for key in fruits:
    d[key] +=1

print(d)

subprocess.run(["git","log","--format=%an"], cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

result = subprocess.run(["git", "log","--oneline"], cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab", capture_output=True, text=True)

if result.returncode != 0: 
    print("The command failed!")
    print(result.stderr)
else :
    print("The code ran smoothly !")
    print(result.stdout)

subprocess.run(['git', 'log', '--oneline'], cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

result = subprocess.run(['git', 'log', '--format=%cd', '--date=short'], capture_output=True, text=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

if result.returncode != 0:
    print(result.stderr)
else: 
    print(result.stdout)

dates_t = subprocess.run(['git', 'log', '--format=%ct'], capture_output=True, text=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

for date in dates_t.stdout.splitlines():
    date = datetime.fromtimestamp(int(date), tz=timezone.utc)
    print(date)

import argparse 

parser = argparse.ArgumentParser(
    description = "Un test"
)
parser.add_argument(
    "--dry-run",
    action='store_true',
    help="Run without performing actual operations"
)
parser.add_argument(
    "name",
    help="Give me you name"
)

args = parser.parse_args()

def justTest(name, dry_run=False):
    if dry_run: 
        print("This is just a dry run")
    else:
        print(f"This is your name : {name}")

justTest(args.name, args.dry_run)

try: 
    result = subprocess.run(['git', 'log', '--oneline'], 
    check=True, 
    capture_output=True, 
    text=True, 
    cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

    print("return code, ", result.returncode)
    print(result.stdout)

except subprocess.CalledProcessError as e: 
    print("Command failed !")
    print("Return code: ", e.returncode)
    print("Command:", e.cmd)
    print("Error:", e.stderr)

from pathlib import Path 

Path("a/b").mkdir(parents=True, exist_ok=True)

pwd =Path("a/b").resolve()

for file in pwd.iterdir():
    if not file.is_file():
        print("There is no file in this folder.")

file = Path(f"{pwd}/file.text")
file.touch()
file.write_text("This is a text.")
print(file.read_text())

for file in pwd.iterdir():
    print(file.stem)
    print(file.name)
    print(file.suffix)


subprocess.run("git log --online", shell=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

for file in pwd.iterdir():
    print(file.exists())

import shutil 

base = Path(r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab").resolve()
print(base)
src = base / "a" / "b" / "file.text"
dst = base / "a" / "file.txt"

if src.is_file():
    shutil.move(src, dst)
    print("moved!")
    shutil.move(dst, src)
    print("moved again !")

src.rename("a/b/file.text")

from collections import Counter 

print(Counter([i for i in "This is a text".split(" ")]).most_common(2))

result = subprocess.run("git log --format=%ct", shell=True, capture_output=True, text=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

for ts in result.stdout.splitlines():
    print(datetime.fromtimestamp(int(ts)).date())

for ts in result.stdout.splitlines():
    print(datetime.fromtimestamp(int(ts), tz=timezone.utc))

def greet(name:str)->str:
    return name

print(greet("Seydou"))

from typing import Optional

def greet(name:Optional[str]=None) -> Optional[str]:
    return name

print(greet())

def greet(name:str="john")->str:
    return name

print(greet())
print(greet("seydou"))

print(tuple[12,2])

def greet(person:tuple[str,int]) -> tuple[str, int]:
    name, age = person
    return f"Ton nom est {name}, tu as {age} ans."

print(greet(("Seydou", 18)))

def greet() -> tuple[str, int]:
    return ("Seydou",25)

print(greet())

from dataclasses import dataclass, field, asdict

@dataclass
class Person: 
    name:str
    age:int 
    inventory:list[str] = field(default_factory=list)
    is_online:bool = True

personne = Person(name="Seydou", age=100, is_online=False)
print(personne)
print(personne.name)
print(type(asdict(personne)))
personne_dict = asdict(personne)
print(personne_dict.get("name"))
@dataclass(frozen=True)
class Person:
    name: str
    age: int 
    is_online: bool = field(default_factory=bool)

personne = Person(name="Seydou", age=12)


import pytest 

def categorize(name):
    if name.suffix() == ".png":
        return "images"
    elif name.suffix() == "py":
        return "code"

@pytest.mark.parametrize(
    "name, expected",
    {
        ("a.png", "images"),
        ("b.py", "code"),
    }
)

def test_category(name, expected):
    assert categorize(name) == expected


def test_x(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("Hello, world!")

    assert file.exists()
    assert file.read_text() == "Hello, world!"

import shutil 

def test_move_file(tmp_path):
    source = tmp_path/"source.txt"
    destination = tmp_path/"destination.txt"

    source.write_text("Test content")
    shutil.move(str(source, str(destination)))

    assert not source.exists()
    assert destination.exists()
    assert destination.read_text() == "text content"

subprocess.run("git log --name-only", shell=True, text=True, cwd=r"C:\Users\skabo\OneDrive\Bureau\Studies\AI - Solo studies\neuro_lab")

age : dict['str', 'int'] = {
    "Seydou": 18,
    "John": 20,
}

print(age.get("Seydou"))
print(age["Seydou"])

path = Path("a")/"b"/"c.txt"

path.parent.mkdir(parents=True, exist_ok=True)
path.touch()

from datetime import datetime

d =datetime.now() 
d.strftime("%Y-%m-%d %H:%M:%S")

from dataclasses import dataclass, field 

@dataclass 
class Person: 
    name: str
    age: str
    inventory:list[str] = field(default_factory=list)

seydou = Person(name="Seydou", age="21", inventory=["apple", "banana", "orange"])
print(seydou.name)
print(seydou.age)
print(seydou.inventory)