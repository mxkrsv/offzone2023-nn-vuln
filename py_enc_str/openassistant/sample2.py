def encryption(string,key):
    """Encrypts the given string with the provided key"""
    cipher_text = ""
    
    #Loop through each character of string 
    for char in string:  
        #Compute the corresponding frequency
        freq = (ord(char) - ord('a')) % 26
        
        #Add offset to compute corresponding letter index
        idx = ((freq + (ord(key[0]))) % 5
        
        #Append character from the encrypted alphabet
        cipher_text += chr(97+idx)
    
    return cipher_text

def decryption(cipher_text,key):
    """Decrypts the given cipher text with the provided key"""
    plaintext = ""
    
    #Convert cipher_text into a list
    lst = [ord(c) for c in cipher_text]
    
    #Loop over the characters
    for i in range(len(lst)-1):
        j = (i-8*int((lst[i]/36)) )%5
        #Get current character index
        indx=j%26
        PlainText = ord(indx)+j%4
      
        plaintext+=chr(PlainText)
    
    return plaintext

if name == 'main':
    print("String Encrypted:",encryption("Hello World!","hello world!"))
    print("String Decrypted: ",decryption(encryption("Hello World!","hello world!"), "hello world!"))
