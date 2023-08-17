from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def sign_message(private_key_pem, message):
    """
    Sign a message using a given ECDSA private key.

    Parameters:
    - private_key_pem (str): The private key in PEM format.
    - message (bytes): The message to be signed.

    Returns:
    - bytes: The signature.
    """

    # Deserialize the private key
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None,
    )

    # Ensure it's an EC private key
    if not isinstance(private_key, ec.EllipticCurvePrivateKey):
        raise ValueError("The provided key is not an ECDSA private key.")

    # Sign the message
    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

    return signature

# Example of using the function
private_key_pem = """
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIOY3vhJ8Q+0DZz1H/jYJHAWVLCu2vyxGjSdQjhRJ0SZBoAoGCCqGSM49
AwEHoUQDQgAEY4IkdHoDdEcvMaK1YcHxv5qYbF0RHCjvX/JOskDP1D8UHxp7qJE/
UwRa2glFtJ2ziT2DWfZxIuCFj+c6Ehf4Hw==
-----END EC PRIVATE KEY-----
"""
message = b"Hello, World!"
signature = sign_message(private_key_pem, message)
print(signature)
