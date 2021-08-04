import pymysql
import random
import os

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             autocommit=True)
                    

with connection.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS CRYPTON;")
    cursor.execute("USE CRYPTON;")                            
    cursor.execute("CREATE TABLE IF NOT EXISTS CIPHER(CRYPT_KEY TEXT, NEW text);")
    os.system('cls')
def cipher(plaintext, n):
    text_key = []
    for i in plaintext:
        text_key.append(ord(i))
    cipher_key = random.randint(10**(n-1), (10**n)-1)
    cipher_key_list = list(map(int,str(cipher_key)))
    text_hidden_key = []
    for i in range(n):
        text_hidden_key.append(text_key[i] + cipher_key_list[i])
    text_hidden = ''
    for i in text_hidden_key:
        text_hidden += (chr(i))
    print('Message Encrypted: ',text_hidden)
    print("Please save this encrypted message to decrypt later if required.")
    sql = "INSERT INTO CIPHER VALUES(%s,%s);"
    
    with connection.cursor() as cursor:  
        cursor.execute(sql,(cipher_key,text_hidden))

def decipher(enc_text_data,enc_text,ln):
    with connection.cursor() as cursor:
        cursor.execute("SELECT CRYPT_KEY FROM CIPHER WHERE NEW = %s" % ("'"+enc_text_data+"'"))
        query = list(cursor.fetchone())
    dec_key = list(query[0])
    enc_text_key = []
    for i in enc_text:
        enc_text_key.append(ord(i))
    output_str = ''
    for i in range(ln):
        output_str += chr(enc_text_key[i]-int(dec_key[i]))
    print("Decryption Complete.")
    print("The decrypted text is: ",output_str)

def exit_code():
    user_input = input("Do you wish to continue? (Y/N): ")
    if user_input.lower() == 'y':
        os.system('cls')
        ui()
    elif user_input.lower() == 'n':
        print("Thank You for using CryptOn.")
        exit()
    else:
        print("Sorry. Invalid Response")
        print("Thank You for using CryptOn.")
        exit()    
    
def ui():
    print("Welcome to CryptOn.")
    response = int(input("Do you want to encrypt or decrypt?(Type for 0 for encryption and 1 for decryption): "))
    if response == 0:
        data = input("Enter word(s) to encrypt: ")
        plaintext = list(map(str,data))
        n = len(plaintext) 
        cipher(plaintext, n)
        exit_code()
        
    elif response == 1:
        enc_text_data = input("Enter the text to decrypt: ")
        enc_text = list(map(str,enc_text_data))
        ln = len(enc_text)
        decipher(enc_text_data,enc_text,ln)
        exit_code()
    else:
        print("Sorry, Invalid response.")
        exit("Thank You for using CryptOn!")

if __name__ == "__main__":
    ui()