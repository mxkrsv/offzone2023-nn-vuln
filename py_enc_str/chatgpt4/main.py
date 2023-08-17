from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def aes_encrypt(data: str, key: bytes) -> (bytes, bytes):
    """
    Encrypts data using AES-CBC.
    
    Parameters:
        data (str): The data to be encrypted.
        key (bytes): The symmetric key. Must be 16, 24, or 32 bytes long.
        
    Returns:
        tuple: Encrypted data and the initialization vector (IV).
    """
    # Convert the data to bytes
    data_bytes = data.encode('utf-8')
    
    # Create a padder object
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data_bytes) + padder.finalize()
    
    # Create a random IV
    iv = os.urandom(16)
    
    # Create the cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    return encrypted_data, iv

def aes_decrypt(encrypted_data: bytes, key: bytes, iv: bytes) -> str:
    """
    Decrypts data encrypted using AES-CBC.
    
    Parameters:
        encrypted_data (bytes): The data to be decrypted.
        key (bytes): The symmetric key. Must be 16, 24, or 32 bytes long.
        iv (bytes): The initialization vector used during encryption.
        
    Returns:
        str: The decrypted data.
    """
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Create an unpadder object
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data_bytes = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    return decrypted_data_bytes.decode('utf-8')
