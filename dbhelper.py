#Dbhelper.py file
#I used a pandas dataframe to store permananent data as csv files, and used os to manipulate other files
import pandas as pd 
import os
from scraper import * #My scraper.py file

df = pd.read_csv('community.csv', index_col=0) #df is the main dataframe which lists every user's email, name, communityID(index of community in settings), and password
settings = pd.read_csv('CommunitySettings.csv', index_col=0) #Settings is the secondary dataframe which lists every communities index, County(location), and community message


def add_df(Email, Name, CommunityID, PW): #Adds a user to the database given email, name, communityID, and password
    global df
    df1 = pd.DataFrame([[Email, Name, CommunityID, PW]], columns=['Email', 'Name', 'CommunityID', 'PW']) #create a new row for the new user's information
    df = df.append(df1, ignore_index=True) #Add row to main dataframe
    if os.path.exists('/Users/sandeep/Documents/Create__Task/community.csv'): #Update csv by deleting old one and creating a new one with the same name
        os.remove('/Users/sandeep/Documents/Create__Task/community.csv')
    df.to_csv("community.csv")


def isUser(username, PW): #Checks if username/pw combo exists
    return (PW == list(df['PW'])[(list(df['Name']).index(username))])

def community_to_ID(community): #Converts community name to ID if exists, else returns -1
    global settings
    comm_list = list(settings['Name'])
    try:
        return(int(comm_list.index(community)))
    except:
        return -1

def UserCommunityName(username):
    user = list(df['Name']).index(username)
    name = settings.loc[df.loc[int(user)]['CommunityID']]['Name']
    county = settings.loc[df.loc[int(user)]['CommunityID']]['County']
    return [name, county]

def UserCommunity(username): #Returns list of members in same community as given username
    user_list = list(df['Name'])
    for i in range(len(user_list)):
        if user_list[i] == username:
            user_index = i
            break
        else:
            None
    cID = df.loc[int(user_index)]['CommunityID']
    return(list(df.loc[df['CommunityID'] == cID]['Name']))

def UserCommunityCases(username): #Number of Cases in community of user
    user = list(df['Name']).index(username)
    cID = df.loc[int(user)]['CommunityID']
    return(scrapeCounty(settings.loc[int(cID)]['County']))

def change_email(username, new_email): #Changed email field for username with new_email
    user = list(df['Name']).index(username) #row index for user
    df.at[user, 'Email'] = new_email #Set email field to new_email
    if os.path.exists('/Users/sandeep/Documents/Create__Task/community.csv'):
        os.remove('/Users/sandeep/Documents/Create__Task/community.csv')
    df.to_csv("community.csv")
    return(df.at[user, 'Email'])

def add_message(username, message):
    user = list(df['Name']).index(username)
    cID = df.loc[int(user)]['CommunityID']
    try:
        settings.at[cID, 'Message'] = message
        if os.path.exists('/Users/sandeep/Documents/Create__Task/CommunitySettings.csv'):
            os.remove('/Users/sandeep/Documents/Create__Task/CommunitySettings.csv')
        settings.to_csv("CommunitySettings.csv")
        return 1
    except:
        return -1
def get_message(username):
    user = list(df['Name']).index(username)
    cID = df.loc[int(user)]['CommunityID']
    return(settings.at[cID, "Message"])


if __name__ == "__main__":
    print(UserCommunity("Test4"))
    #print(settings)