import hashlib
from ecdsa import SigningKey, SECP256k1

def sign_message(message, private_key_hex):
    """
    Sign a message using ECDSA and the given private key.
    
    :param message: The message to be signed.
    :param private_key_hex: The ECDSA private key in hexadecimal format.
    :return: The signature in hexadecimal format.
    """
    # Convert the private key from hex to bytes
    private_key_bytes = bytes.fromhex(private_key_hex)
    
    # Create a signing key object from the private key bytes
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    
    # Hash the message using SHA-256
    message_hash = hashlib.sha256(message.encode()).digest()
    
    # Sign the message hash
    signature = sk.sign(message_hash)
    
    # Return the signature in hexadecimal format
    return signature.hex()
