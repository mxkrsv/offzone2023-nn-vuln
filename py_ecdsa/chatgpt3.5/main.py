from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils

def sign_message(message, private_key):
    try:
        private_key_bytes = private_key.encode('utf-8')  # Assuming private_key is provided as a string
        private_key_obj = serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())
        
        signature = private_key_obj.sign(
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        
        return signature.hex()
    except Exception as e:
        return str(e)

# Example usage
private_key = """-----BEGIN EC PRIVATE KEY-----
# Your EC private key goes here
-----END EC PRIVATE KEY-----"""

message_to_sign = "This is the message to sign."

signature = sign_message(message_to_sign, private_key)
print("Signature:", signature)
