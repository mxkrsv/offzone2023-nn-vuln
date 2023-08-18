import os

def get_file(path):
    if path.startswith("/safedir/"):
        return open(path)
    else:
        raise ValueError("File path must start with /safedir/")

# Usage:
safe_dir = "/safedir"
try:
    with get_file(safe_dir + "my_file.txt") as f:
        print(f.read())
except ValueError as e:
    print("Error accessing file:", e)
