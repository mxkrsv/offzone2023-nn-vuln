from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a random symmetric key for encryption and decryption.
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Encrypts a given message using the provided symmetric key.

    Args:
        message (str): The message to be encrypted.
        key (bytes): The symmetric key used for encryption.

    Returns:
        bytes: The encrypted message.
    """
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Decrypts a given encrypted message using the provided symmetric key.

    Args:
        encrypted_message (bytes): The encrypted message to be decrypted.
        key (bytes): The symmetric key used for decryption.

    Returns:
        str: The decrypted message.
    """
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
if name == "main":
    symmetric_key = generate_key()
    message_to_encrypt = "This is a secret message."

    encrypted_message = encrypt_message(message_to_encrypt, symmetric_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, symmetric_key)
    print("Decrypted Message:", decrypted_message)
