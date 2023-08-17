import os

class FileAccessError(Exception):
    """Exception raised for trying to access files outside of allowed directory."""
    pass

def get_file_from_path(path: str):
    # Normalize the path to ensure it's an absolute path
    normalized_path = os.path.abspath(path)

    # Check if the path is inside the allowed directory
    if not normalized_path.startswith("/safedir"):
        raise FileAccessError(f"Access to '{normalized_path}' is not allowed. Only files within '/safedir' can be accessed.")
    
    # Check if the file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"No file found at '{normalized_path}'.")
    
    return open(normalized_path, 'r')
