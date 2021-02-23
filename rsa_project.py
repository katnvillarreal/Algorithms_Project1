# Algorithms RSA Project
# Members: Kathryn Villarreal
#          Monique Dashner
#          Kile Adams

import random as rn
import math

# Use this to generate the private key
def extended_gcd(a=1, b=1):
    if b ==0:
        return(1,0,a)
    (x,y,d) = extended_gcd(b, a%b)
    return y, x-a//b*y, d 

def gen_keys():
    randoms = [rn.randint(1000, 10000) for i in range(100)]
    primes = set()
    for i in range(5):
        for j in randoms:
            if pow(rn.randint(2,100), j - 1, j) ==1:
                primes.add(j)

    primes = list(primes)
    p = primes[0]
    q = primes[1]
    n = p*q
    f = (p-1)*(q-1)
    e = 3
    # Generate e
    for i in range(2, len(primes)):
        if math.gcd(primes[i], f) == 1:
            e = primes[i]
            break
    (d, x, y) = extended_gcd(e, f)

    return p, q, n, f, e, d

def encrypt_message(message, e, n):
    # Given a message string encrypt it using the public key

    # Convert string into an array and convert the characters into numbers (Based on ascii)
    # pow(ascii value of character, e, n) 
    # convert back to characters
    # return encrypted message
    encrypted = list()
    for i in range(len(message)):
        if isinstance(message[i], str):
            new_char = pow((ord(message[i])),e,n)
        else:
            new_char = pow(message[i],e,n)
        try:
            encrypted.append(chr(new_char))
        except:
            encrypted.append(new_char)
    return encrypted

def decrypt_message(message, d, n):
    # Given an encrypted message decrypt it using the private key

    # Convert the string array into an integer array (based on ascii)
    # pow(ascii value of character, d, n) 
    # convert back to characters
    # return the decryted message
    decrypted = list()
    for i in range(len(message)):
        if isinstance(message[i], str):
            new_char = pow((ord(message[i])),d,n)
        else:
            new_char = pow(message[i],d,n)
        try:
            decrypted.append(chr(new_char))
        except:
            decrypted.append(new_char)
    return decrypted

def create_signature(signature, d, n):
    # Given a signature, encrypt it using the private key

    # convert string array to integer array
    # (int^d)%n = encrypted signature
    # return encrypted signature
    encrypted = list()
    for i in range(len(signature)):
        if isinstance(signature[i], str):
            new_char = pow((ord(signature[i])),d,n)
        else:
            new_char = pow(signature[i],d,n)
        try:
            encrypted.append(chr(new_char))
        except:
            encrypted.append(new_char)
    return encrypted

def decrypt_signature(signature, e, n):
    # Given a signature, decrypt it using the public key

    # convert string array to integer array
    # (int^e)%n = decrypted signature
    # return decryped signature
    decrypted = list()
    for i in range(len(signature)):
        if isinstance(signature[i], str):
            new_char = pow((ord(signature[i])),e,n)
        else:
            new_char = pow(signature[i],e,n)
        try:
            decrypted.append(chr(new_char))
        except:
            decrypted.append(new_char)
    return decrypted

if __name__ == "__main__":
    # Create the private and public keys
    (p,q,n,f,e,d) = gen_keys()

    print("P: "+ str(p))
    print("Q: "+ str(q))
    print("N: "+ str(n))
    print("F: "+ str(f))
    print("E: "+ str(e))
    print("D: "+ str(d))

    encrypted = encrypt_message("butts", e, n)
    decrypted = decrypt_message(encrypted, d, n)
    e_sig = create_signature("Alice", d, n)
    v_sig = decrypt_signature(e_sig, e, n)

    print("Encryted message: " + str(encrypted))
    print("Decryted message: " + str(decrypted))
    print("Encryted signiture: " + str(e_sig))
    print("Decryted signiture: " + str(v_sig))
    

    # Have the user choose between being a owner or public user
    # If Owner
    #   Prompt to either decrypt or create a digital signature
    #   If Decrypt messasge
    #       Have a message that is either made by a public user or a preset message
    #       Print the encrypted message
    #       Decrypt the message
    #       Print the decrypted message
    #   If create a digital signature
    #       Have the user enter a signature
    #       Encrypt it with the private key
    # If Public User
    #   Prompt to encrypt or verify signature
    #   If Encrypt message
    #       Have the user enter a message
    #       Encrypt the message with the public key
    #       Print the encrypted message
    #   If Verify Signature
    #       Have an encrypted signature 
    #       Decrypt the signature with the public key
    #       Print out the decrypted signature