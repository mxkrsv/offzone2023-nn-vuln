from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
    decode_dss_signature
)

def sign_ecdsa(message, private_key):
    try:
        # Load the private key from PEM format
        private_key_obj = serialization.load_pem_private_key(
            private_key.encode('utf-8'),
            password=None,
            backend=default_backend()
        )

        # Sign the message
        signature = private_key_obj.sign(
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )

        # Return the encoded signature
        r, s = decode_dss_signature(signature)
        return encode_dss_signature(r, s)

    except Exception as e:
        print("Error:", e)
        return None

# Example usage
private_key_pem = """
-----BEGIN EC PRIVATE KEY-----
# Your EC private key in PEM format
-----END EC PRIVATE KEY-----
"""

message_to_sign = "This is a test message."
signature = sign_ecdsa(message_to_sign, private_key_pem)

if signature:
    print("Message:", message_to_sign)
    print("ECDSA Signature:", signature)
