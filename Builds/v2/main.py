import engine
import profiles
import routines
def user_management():
    print(routines.logo)
    print("Hi!")
    response1=(int(input("Do you have an account? (Y|N): "))).lower()
    if response1 == 'y':
        profiles.login()
    elif response1 == 'n':
        profiles.signup()
    else:
        routines.invalid_res()



    