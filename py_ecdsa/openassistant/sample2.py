def sign_ecdsa(message, private_key):
    from ecdsa import SigningContext
    context = SigningContext()
    signature = context.sign(private_key, message)
    return signature
