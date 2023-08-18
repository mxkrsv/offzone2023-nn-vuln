def encrypt(key, data):
    """This function will take an encryption key and data as input, it
    then returns a new dictionary with all of our values encrypted"""
    
    # Create a copy of the original dictionary
    result = dict(data)
    
    # Iterate through each value to encode
    for k, v in list(result.items()):
      if isinstance(v, str):
        result[k] = v.encode('utf-8')
        
    return result

def decrypt(key, data):
    """This function takes an decryption key and decrypted data
    as input, it then returns a dictionary with all of its values decoded"""
    
    # Create a copy of the original dictionary
    result = dict(data)
    
    # Iterate through each value to decode
    for k, v in list(result.items()):
      if isinstance(v, bytes):
        result[k] = v.decode('utf-8')
        
    return result
