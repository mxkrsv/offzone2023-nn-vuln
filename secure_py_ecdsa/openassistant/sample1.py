from ecdsa import SigningKey, PrivateKey, hash_160, SHA256

# Generate a private key and public key from the provided input
key = PrivateKey(input)
public_key = PublicKey(key.public_point())

# Compute the signature for the given message
def compute_signature(message):
    # Append the hash prefix and the message itself to the signing key
    signing_private = PrivateKey(key.private_point().public(), passphrase=passphrase)
    h = hash_160("ECDSA-SHA256", str_to_bytes(message))
    
    sig = PrivateKey(str_to_bytes(h[1]) + public_key.serialize()).sign(message)
    return SHA256.hash(sig).hexdigest()

