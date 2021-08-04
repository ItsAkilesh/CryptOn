import dbman
import random
import os
import profiles

def encrypt(username=profiles.username):
    string = input("Enter the word(s) you want to encrypt: ")
    string_ord = []; n = len(string)
    task = [string_ord.append(ord(i)) for i in list(string)]
    enc_key = list(str(random.randint(10**(n-1), (10**n)-1)))
    enc_string = ''
    for i in range(len(string)):
        x = string_ord[i]+int(enc_key[i])
        enc_string += chr(x)
    dbman.cursor.execute("INSERT INTO CRYPT VALUES({username},{enc_string},{enc_key});")
    print("Your text is encrypted. You may need this to decrypt the text later: {enc_string}")  
def decrypt(username=profiles.username):
    pass

