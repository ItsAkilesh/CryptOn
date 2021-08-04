import dbman
import random
import create_db
import routines
import pickle

def encrypt(username):
    string = input("Enter the word(s) you want to encrypt: ")
    string_ord = []; n = len(string)
    task = [string_ord.append(ord(i)) for i in list(string)]
    enc_key_list = list(str(random.randint(10**(n-1), (10**n)-1)))
    enc_string = ''
    for i in range(len(string)):
        x = string_ord[i]+int(enc_key_list[i])
        enc_string += chr(x)
    enc_key = ''
    for i in enc_key_list:
        enc_key+=i
    enc_key = int(enc_key)
    dbman.cursor.execute(f"INSERT INTO {username} VALUES(%s,%s);",(enc_string,enc_key))
    with open('failsafe.dat', 'rb+') as failsafe:#Failsafe
        r = pickle.load(failsafe)
        r['enc_string'] = enc_key
    with open('failsafe.dat', 'wb') as failsafe:
        pickle.dump(r,failsafe)        
    print("Your text is encrypted. You may need this to decrypt the text later:",enc_string)  

def decrypt(username):
    string = input("Enter the encrypted text: ")
    string_ord = []; n = len(string)
    task = [string_ord.append(ord(i)) for i in list(string)]
    dbman.cursor.execute(f"Select * from {username};")
    task2 = dict(dbman.cursor.fetchall())
    with open('failsafe.dat','rb') as failsafe:
        task3 = pickle.load(failsafe)
    if string in task2.keys():
        enc_key = task2[string]
        enc_key_list = list(str(enc_key)) 
        dec_string = ''
        for i in range(n):
            x = string_ord[i]-int(enc_key_list[i])
            dec_string += chr(x)
        print("Your text has been decrypted: ",dec_string,'\n ')
    elif string in task3.keys():
        print("Your text has been decrypted: ",task3[string],'\n')
    elif string not in task2.keys():
        print("No record found. Please try again.")
        decrypt(username)
    
def signup():
    dbman.cursor.execute("Select * from Profiles;")
    unique_check = dict(dbman.cursor.fetchall())
    username = (input("Enter username: ")).strip()
    if username in unique_check.keys():
        print("Username Taken. Please try again.")
        signup()
    else:
        password = input("Enter a unique password: ")
        q = "INSERT INTO PROFILES VALUES(%s,%s);"
        dbman.cursor.execute(q,(username,password))
        create_db.users(username)
        routines.cls()
        print('Successfully signed up!')
        ui(username)  
          
def login():
    username = (input("Enter username: ")).strip()
    dbman.cursor.execute("Select * from Profiles;")
    cred_check = dict(dbman.cursor.fetchall())
    if username in cred_check.keys():
        password = input("Enter password: ")
        if cred_check[username] == password:
            ui(username)
        elif cred_check[username] != [password]:
            routines.login_err()
            login()
    elif username not in cred_check.keys():
        print(f"Username {username} not found!! Try again.")
        login()

def ui(username):
    print(f"Welcome {username}. What would you like to do?")
    response2=input("Encryption or Decryption? (Enter 1 or 2): ")
    if response2 == '1':
        encrypt(username)
        response3 = (input("Do you wish to continue? (Y|n): ")).lower()
        if response3 == 'y':
            ui(username)
        elif response3 == 'n':
            exit("Thank you for using CryptOn.")      
        else:
            routines.invalid_res()      
    elif response2 == '2':
        decrypt(username)
        response3 = (input("Do you wish to continue? (Y|n): ")).lower()
        if response3 == 'y':
            ui(username)
        elif response3 == 'n':
            print(routines.logo,'\n')
            exit("Thank you for using CryptOn.")
        else:
            routines.invalid_res()
    else:
        routines.invalid_res()

