from Crypto.Cipher import AES
￼
def aes_encrypt(plaintext,key):
    # Encode plaintext as bytes
    plaintxt_bytes = plaintext.encode("utf8")
    
    # Derive the initialization vector (IV) from the key
    iv = SHA256.new(key).digest()[:AES.block_size]

    # Create cipher object with AES-ECB mode
    cipher = AES.new(None, MODES['ecb'], None, len(plaintxt_bytes))

    # Pad the plaintext before encrypting it
    padder = PKCS7Encoder(cipher).asn1Object().rawContent[0].content[1].value
    padded_plaintext = plaintxt_bytes + bytes([padder])

    # Perform actual encryption
    return cipher.encrypt(padded_plaintext)

def aes_decrypt(encrypted_data, key):
    # Decode encrypted data into bytes
    encrypted_data_bytes = encrypted_data.decode("hex").bytes

    # Extract IV from encrypted data
    iv = encrypted_data_bytes[0 : AES.block_size]

    # Create cipher object with AES-ECB mode
    cipher = AES.new(None, MODES['ecb'], None, len(encrypted_data)-AES.block_size)

    # Unpadding the encrypted data
    unpadding = PAD.unpad(encrypted_data_bytes, len(encrypted_date
