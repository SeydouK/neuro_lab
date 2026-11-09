import subprocess
from collections import Counter
from datetime import datetime


def run_git_command(args):
    result = subprocess.run(
        ["git"] + args, 
        capture_output=True, 
        test=True, 
        check=True
    )

    return result.stdout

def commit_per_day():
    output = run_git_command(
        ["log", "--format=%cs"]
    )
    dates = output.splitlines()

    counts = Counter(dates)

    print("\n--- Commits per day ---")
    for day, count in sorted(counts.items()):
        print(f"{day}: {count} commit(s)")

def most_changed_files():
    output = run_git_command(
        ["log", "--format=", "--name-only"
    ])

    files = [
        line for line in output.splitlines()
        if line.strip()
    ]

    counts = Counter(files)

    print("\n--- Most-changed files ---")
    for filename, count in counts.most_common(10):
        print(f"{filename}: {count} change(s)")

def longest_gap():
    output = run_git_command(["log", "--format=%ct"])
    timestamps = sorted(
        int(line) for line in output.splitlines()
        if line.strip()
    )

    print("\n--- Longest gap between commits ---")

    if len (timestamps) < 2:
        print("Not enoguh commits to calculate a gap.")
        return 

    longest = 0 
    gap_start = None 
    gap_end = None 

    for earlier, later in zip(timestamps, timestamps[1:]):
        gap = later - earlier

        if gap > longest:
            longest = gap 
            gap_start = earlier 
            gap_end = later 

    start = datetime.fromtimestamp(gap_start)
    end = datetime.fromtimestamp(gap_end)

    print(f"From: {start}")
    print(f"To: {end}")
    print(f"Gap: {longest/86400:.2f} days")


def main():
    try:
        commits_per_day()
        most_changed_files()
        longest_gap()
    except subprocess.CalledProcessError:
        print("Error: Could not run Git. Are you inside a Git repository?")
    except FileNotFoundError:
        print("Error: Git is not installed or is not on your PATH.")


if __name__ == "__main__":
    main()
