import os

def open_file_in_safedir(path):
    safe_directory = "/safedir"
    
    # Check if the given path is within the safe directory
    if not path.startswith(safe_directory):
        raise ValueError("Access to files outside of safe directory is not allowed.")
    
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file at '{path}' does not exist.")
    
    # Open the file and return the File object
    file = open(path, "r")  # You can change the mode ("r", "w", "a", etc.) as needed
    return file

# Example usage
try:
    file_path = "/safedir/example.txt"
    file_obj = open_file_in_safedir(file_path)
    print(file_obj.read())  # Read and print the content of the file
    file_obj.close()        # Close the file when done
except ValueError as ve:
    print(ve)
except FileNotFoundError as fnfe:
    print(fnfe)
