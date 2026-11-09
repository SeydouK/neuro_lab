import argparse
from organizer.core import organize

parser = argparse.ArgumentParser(
    description="This is an organizer."
)

parser.add_argument(
    "--cwd",
    help="The path of the folder."
)
args = parser.parse_args()

print(organize(args.cwd))