import engine
import dbman
import routines

def signup():
    global username
    username = input("Enter a unique username: ")
    dbman.cursor.execute("Select * from Profiles;")
    unique_check = dbman.cursor.fetchall()
    if username not in unique_check:
        password = input("Enter a unique password: ")
        dbman.cursor.execute("INSERT INTO PROFILES VALUES({username},{password});")
        print('Successfully signed up!')
    ui(username)    

def login():
    global username
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    dbman.cursor.execute("Select * from Profiles;")
    cred_check = cursor.fetchall()
    if cred_check[username] == password:
        ui(username)
    else:
        routines.login_err()
        login()
   

def ui(username):
    print("Welcome {username}. What would you like to do?")
    response2=int(input("Encryption or Decryption? (Enter 1 or 2): "))
    if response2 == 1:
        engine.encrypt()
    elif response2 == 2:
        engine.decrypt()
    else:
        routines.invalid_res()
