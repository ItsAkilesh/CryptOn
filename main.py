import engine
import routines
import create_db

create_db.create()
create_db.db_select()
create_db.profiles()
routines.cls()

def app():
    try:
        print(routines.logo)
        print("Hi!")
        response1=(input("Do you have an account? (Y|N): ")).lower()
        if response1 == 'y':
            engine.login()
        elif response1 == 'n':
            engine.signup()
        else:
            routines.invalid_res()
    except KeyboardInterrupt:
        print("\n\n\n\nKeyBoard Interrupt Detected.\nThank you for using CryptOn. We hope to See you again.")
        print(routines.logo)
        exit(0)
    
    