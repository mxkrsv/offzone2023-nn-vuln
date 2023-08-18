import os

def get_file(path):
  if path.startswith("/safedir/"):
    raise ValueError("Path must not start with '/safedir/'")
  return open(path, "r")
