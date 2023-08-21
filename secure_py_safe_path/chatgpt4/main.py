import os

class FileAccessError(Exception):
    pass

class File:
    def __init__(self, path):
        self.path = path

    # Add more methods if needed to interact with the file.
    # For instance, read(), write(), etc.

def get_file_from_path(path):
    # Make sure the path is absolute
    abs_path = os.path.abspath(path)
    
    # Ensure the path is normalized, removing any "..", ".", etc.
    normalized_path = os.path.normpath(abs_path)
    
    if not normalized_path.startswith("/safedir"):
        raise FileAccessError(f"Access to the file '{path}' is restricted!")

    return File(normalized_path)

# Example Usage
try:
    file_obj = get_file_from_path("/safedir/subdir/myfile.txt")
    print(f"Access granted to: {file_obj.path}")
except FileAccessError as e:
    print(e)
