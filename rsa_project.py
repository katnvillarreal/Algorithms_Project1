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
    randoms = [rn.randint(10000, 100000) for i in range(100)]
    primes = set()
    for i in range(5):
        for j in randoms:
            if pow(rn.randint(2,100), j - 1, j) ==1:
                primes.add(j)
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
    (x,y,d) = extended_gcd(e, f)

    return p, q, n, f, e, d

def encrypt_message(message, e, n):
    # Given a message string encrypt it using the public key

    # Convert string into an array and convert the characters into numbers (Based on ascii)
    # Raise each of the numbers by e
    # take each of the numbers and perform % n 
    # convert back to characters
    # return encrypted message
    return 0

def decrypt_message(message, d, n):
    # Given an encrypted message decrypt it using the private key

    # Convert the string array into an integer array (based on ascii)
    # Raise each of the numbers to d
    # take each of the numbers and perform % n 
    # convert back to characters
    # return the decryted message
    return 0

def create_signature(signature, d, n):
    # Given a signature, encrypt it using the private key

    # convert string array to integer array
    # (int^d)%n = encrypted signature
    # return encrypted signature
    return 0

def decrypt_signature(signature, e, n):
    # Given a signature, decrypt it using the public key

    # convert string array to integer array
    # (int^e)%n = decrypted signature
    # return decryped signature
    return 0

if __name__ == "__main__":
    # Create the private and public keys
    (p,q,n,f,e,d) = gen_keys()

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