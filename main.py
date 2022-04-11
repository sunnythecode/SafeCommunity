#python -m pip install beautifulsoup4
from hashlib import new
from dbhelper import *
from scraper import *

def login():
    print("\n")
    print("-------LOGIN-------")
    username = input("Username: ")
    password = input("Password: ")
    signup = input("Signup? (y(add accounut)/n(login)): ")
    if signup in ["y", "Y", "Yes", "yes"]:
        email = input("Email: ")
        community = input("Community: ")
        try:
            add_df(email, username, community_to_ID(community), password)
            print("OK!")
            return [1, username]
        except:
            print("error signing in")
            login()
    elif signup in ["n", "N", "No", "no"]:
        if isUser(username, password):
            print('OK!')
            return [1, username]
        else:
            print("Incorrect Login Information")
            login()
    else: 
        print('please type yes or no')
        


def Dashboard(username, county_data):
    print('\n')
    print("-------DASHBOARD-------")
    print('Community Members:')
    print(UserCommunity(username))
    print('TODAYS CASES:' + str(county_data) + '\n')
    print('\n')
    print('1 Settings')
    print('2 Logout')
    print('3 Alert Community')
    exit = input("Enter 1/2/3: ")
    return exit

def Community_Alert():
    print("-------Alert Community-------")
    print("Type Message to be sent:")
    message = input()

def Settings(username):
    print("-------Settings-------")
    print("Change email: ")
    new_email = input("Enter new email here: ")
    change_email(username, new_email)
    return 1


def loop():
    login_value = login()
    print("Loading...")
    user_county_data = UserCommunityCases(login_value[1])
    if login_value[0] == 1:
        dash_value = Dashboard(login_value[1], user_county_data)
        if dash_value == 1:
            sett = Settings(login_value[0])


login_value = login()
print("Loading...")
user_county_data = UserCommunityCases(login_value[1])
if login_value[0] == 1:
    dash_value = Dashboard(login_value[1], user_county_data)
    if dash_value == 1:
        sett = Settings(login_value[0])
    elif dash_value == 2:
        login()
    
