import argparse
import subprocess
import sys 

parser = argparse.ArgumentParser(
    description="Install a Python package and freeze requirements."
)

parser.add_argument("--package", help="Name of the Python package to install.")

args = parser.parse_args()

if args.package:
    subprocess.run(
        [sys.executable, "-m", 'pip', 'install', args.package], 
        check=True
    )

    with open("requirements.txt", "w") as file: 
        subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            stdout=file,
            check=True
        )

    print("Packaging installed and requirements.txt updated.")

else:
    print("No package specified. Use --package PACKAGE_NAME.")