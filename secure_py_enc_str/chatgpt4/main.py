from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a key for encryption and decryption.
    This should be kept secure. Anyone with the key can decrypt data encrypted with this key.
    """
    return Fernet.generate_key()

def encrypt_string(s, key):
    """
    Encrypts the given string with the given symmetric key.

    Args:
    - s (str): The string to be encrypted.
    - key (bytes): The symmetric key.

    Returns:
    - bytes: The encrypted string.
    """
    cipher = Fernet(key)
    encrypted_string = cipher.encrypt(s.encode())
    return encrypted_string

def decrypt_string(encrypted_string, key):
    """
    Decrypts the given encrypted string using the given symmetric key.

    Args:
    - encrypted_string (bytes): The encrypted string to be decrypted.
    - key (bytes): The symmetric key.

    Returns:
    - str: The decrypted string.
    """
    cipher = Fernet(key)
    decrypted_string = cipher.decrypt(encrypted_string).decode()
    return decrypted_string

# Example usage:

key = generate_key()
encrypted = encrypt_string("Hello, World!", key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_string(encrypted, key)
print(f"Decrypted: {decrypted}")
