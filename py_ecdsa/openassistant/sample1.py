def sign_message(key, message):
    h = hashlib.sha256()
    m = message.encode('utf-8')
    s = str(h.digest())
    signature = rsa.sign(m + h.digest(), padding.OAEP, rsa.HashAlgs[0], pkcs7.Padding.PKCS7v15_31Bits)
    return signature
