import os

class SecureFileAccessError(Exception):
    pass

class SecureFile:
    def init(self, path):
        self.path = path
        if not self.is_path_secure():
            raise SecureFileAccessError("Access to this file is not allowed.")

    def is_path_secure(self):
        safe_directory = "/safedir"
        return os.path.abspath(self.path).startswith(safe_directory)

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def write(self, content):
        with open(self.path, 'w') as file:
            file.write(content)

def get_secure_file(path):
    try:
        secure_file = SecureFile(path)
        return secure_file
    except SecureFileAccessError as e:
        print("Secure file access error:", e)
        return None

# Example usage
path = "/safedir/example.txt"
secure_file = get_secure_file(path)
if secure_file:
    content = secure_file.read()
    print("File content:", content)
