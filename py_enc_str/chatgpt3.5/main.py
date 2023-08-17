from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
if name == "main":
    symmetric_key = generate_key()
    message_to_encrypt = "Hello, this is a secret message!"

    encrypted = encrypt_message(message_to_encrypt, symmetric_key)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted, symmetric_key)
    print("Decrypted:", decrypted)
