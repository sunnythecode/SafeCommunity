# MAIN.PY

from dbhelper import *
from scraper import *
from stateHelper import *

#Login function for user
def login():
    print("\n")
    print("-------LOGIN-------")
    username = input("Username: ")
    password = input("Password: ")
    signup = input("Signup? (y(add accounut)/n(login)): ")
    if signup in ["y", "Y", "Yes", "yes"]:
        #Ask for email/community in order to save to csv database
        email = input("Email: ")
        community = input("Community: ")
        try: #Avoid errors being printed in terminal
            add_df(email, username, community_to_ID(community), password) #Function defined in dbhelper.py, tries to add row for user
            print("OK!")
            return [1, username] #Exit code and username cache for the dashboard function to use
        except:
            print("error signing in")
            return login() #Restart function in case of improper inputs
    elif signup in ["n", "N", "No", "no"]:
        try:
            if isUser(username, password):
                print("OK")
                return [1, username]
        except:
            print("incorrect login info")
            return login() # Restart function in case of wrong login credentials
    else: 
        print('please type yes or no')
        return login() #Restart function in case of unclear selection
        

#Dashboard function
# Displays county data, other community members, and option to go to settings, logout, alert community
def Dashboard(username, county_data):
    print('\n')
    print("-------DASHBOARD-------")
    communityName = UserCommunityName(username)[0]
    county = UserCommunityName(username)[1]
    print("Community: " + communityName)
    print("Location: " + county)
    print('Community Members:')
    print(UserCommunity(username)) #Function defined in dbhelper, gets all other users within the same community
    print('TODAYS CASES:' + str(county_data) + '\n')
    print("Message: " + '\n'  + get_message(username))
    print('\n')
    print('1 Settings')
    print('2 Logout')
    print('3 Alert Community')
    print('4 View State Info')
    choice = input("Enter 1/2/3/4: ")
    if not(choice in ['1', '2', '3', '4']):
        print("Please enter an option from 1-4")
        return Dashboard() #Restart function in case of improper input
    else: 
        return choice #Exit code used to choose next function


#Community Alert will allow User to send message to community members, which will be displayed in dashboard 
def Community_Alert(username):
    print("-------Alert Community-------")
    print("Type Message to be sent:")
    message = input()
    add_message(username, message)
    #ToDo: Add message column, add dbhelper function


#Update email address in settings
def Settings(username):
    print("-------Settings-------")
    print("Change email: ")
    new_email = input("Enter new email here: ")
    change_email(username, new_email) #Function in dbhelper changes email field of user's row to new_email
    return 1


def update():
    print("What is your state? (ex Arizona)")
    myState = input()
    today = getDateAndFormat(2)
    yesterday = getDateAndFormat(3)
    #Formats the date fetching the date from a library called dateTime. Data is from yesterday

    TodayRes = scrapeState(today)
    YesterdayRes = scrapeState(yesterday)
    #Scrape takes in a date and returns the data from all states for that date Scraping is done using a library called BeautifulSoup4

    todaysInfo = arrange(TodayRes)
    yesterdaysInfo = arrange(YesterdayRes)
    #Sorts the data into format [STATE NAME, COUNTRY, LAT, LONG, CASES, DEATHS, etc] for all states, returns a list of statesLists 

    stateInfo = findState(myState, todaysInfo)
    yesterStateInfo = findState(myState, yesterdaysInfo)
    #Given a state name, returns it's data

    dailySummary(stateInfo, yesterStateInfo)
    #Prints data fetched from the list. Yesterday is subtracted from today to get the daily deaths.


def app_loop(user): #Function loops dashboard, settings, and community alert functions for the user allowing for navigation
    print('Loading...')
    user_county_data = UserCommunityCases(user)
    dash_choice = Dashboard(user, user_county_data)
    if dash_choice == '2':
        new_user = login()[1]
        return app_loop(new_user)
    elif dash_choice == '1':
        Settings(user)
        app_loop(user)
    elif dash_choice == '3':
        Community_Alert(user)
        app_loop(user)
    elif dash_choice == '4':
        update()
username = login()[1]
app_loop(username)

# End of main.py
