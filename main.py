#python -m pip install beautifulsoup4
from dbhelper import *
<<<<<<< Updated upstream
from stateHelper import *

###DISCLAIMER -- Cases and death information is based off of a similar dataset to google. Google uses the same dataset for certain places, but differs in others.

f = open('StateSaver.txt', 'r')
contents= f.read()
print("Your State Is Currently: " + str(contents))
stateG = str(contents)
=======
from scraper import *
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
def changeState():
  print("What is your state? (ex Arizona)")
  x = input()
  global stateG 
  stateG = str(x)
  
#login_value = login()
#if login_value == 1:
#    dash_value = Dashboard()
#    if dash_value == 1:
#       comm = Community_View()



today = getDateAndFormat(1)
yesterday = getDateAndFormat(2)

TodayRes = scrapeState(today)
YesterdayRes = scrapeState(yesterday)

todaysInfo = arrange(TodayRes)
yesterdaysInfo = arrange(YesterdayRes)

stateInfo = findState(stateG, todaysInfo)
yesterStateInfo = findState(stateG, yesterdaysInfo)

dailySummary(stateInfo, yesterStateInfo)

#Must be last in order to correctly save the state of the user.

changeState()

file1 = open("StateSaver.txt", "w") 
str1 = str(stateG)
file1.write(str1)
file1.close()



=======
login_value = login()
user_county_data = scrapeCounty(login_value[1])
if login_value[0] == 1:
    dash_value = Dashboard(login_value[1], user_county_data)
    if dash_value == 1:
        comm = Community_View()
>>>>>>> Stashed changes
