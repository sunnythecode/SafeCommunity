#python -m pip install beautifulsoup4
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
            return 1
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
    print('USERS:')
    print(county_data)
    print('\n')
    print('TODAYS CASES: ')
    print(UserCommunityCases(username))
    print('\n')
    print('1 Settings')
    print('2 Logout')
    input("Enter 1/2: ")
    return 1

def Community_View():
    print("Community_View")

login_value = login()
user_county_data = scrapeCounty(login_value[1])
if login_value[0] == 1:
    dash_value = Dashboard(login_value[1], user_county_data)
    if dash_value == 1:
        comm = Community_View()
