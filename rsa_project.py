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

# Have the user choose between being a owner or public user
    user = input("Are you a Owner(O) or a Public user(P): ")

# If Owner
    if user == 'O':

    # Prompt to either decrypt or create a digital signature
        owner_user_choice = input("Would you like to decrypt(de) or create a digital signature(di): " )

    # If Decrypt message
        if owner_user_choice == "de":

        # Have a message that is either made by a public user or a preset message
            owner_user_message = input("Please enter message that you would like to decrypt: ")
        # Print the encrypted message
            print("Encryted message: " + str(owner_user_message))
        # Decrypt the message
            decrypt_message(owner_user_message, d, n)
        # Print the decrypted message
            print("Decryted message: " + str(decrypted))

    # If create a digital signature
        if owner_user_choice == "di":

        # Have the user enter a signature
            owner_user_signature = input("Please enter digital signature that you would like to encrypt: ")
        # Encrypt it with the private key
            owner_user_signature = create_signature(owner_user_signature, d, n)
        # Print signature that was created
            print("Encryted signiture: " + str(owner_user_signature))

# If Public User
    if user == 'P':
    # Prompt to encrypt or verify signature
        public_user_choice = input("Would you like to encrypt a message(m) or verify a signature(s)?")

    # If Encrypt message
        if public_user_choice == 'm':

        # Have the user enter a message
            public_user_message = input("Please enter a message that you would like to encrypt: ")
        # Encrypt the message with the public key
            encrypt_message(public_user_message, e, n)
        # Print the encrypted message
            print("Encryted message: " + str(public_user_message))

    # If Verify Signature
        if public_user_choice == 's':

        # Have an encrypted signature
            public_user_signature = input("Please enter digital signature that you would like to decrypt: ")
        # Decrypt the signature with the public key
            public_user_signature = decrypt_signature(public_user_signature, e, n)
        # Print out the decrypted signature
            print("Decrypted signature: " + str(public_user_signature))