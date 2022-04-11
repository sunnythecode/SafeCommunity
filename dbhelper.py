
import pandas as pd
import os
from scraper import *
df = pd.read_csv('community.csv', index_col=0)
settings = pd.read_csv('CommunitySettings.csv', index_col=0)

def add_df(Email, Name, CommunityID, PW):
    global df
    df1 = pd.DataFrame([[Email, Name, CommunityID, PW]], columns=['Email', 'Name', 'CommunityID', 'PW'])
    #print(df1)
    df = df.append(df1, ignore_index=True)
    if os.path.exists('/Users/sandeep/Documents/Create__Task/community.csv'):
        os.remove('/Users/sandeep/Documents/Create__Task/community.csv')
    df.to_csv("community.csv")


def isUser(username, PW):
    return (PW == list(df['PW'])[(list(df['Name']).index(username))])

def community_to_ID(community):
    global settings
    comm_list = list(settings['Name'])
    try:
        return(int(comm_list.index(community)))
    except:
        return -1

def add_community(Name, CovidAlert, County):
    global settings
    if community_to_ID(Name) == -1:
        df1 = pd.DataFrame({"Name":[Name],
                            "CovidAlert":[CovidAlert],
                            "County":[County]
                            })
        settings = settings.append(df1, ignore_index=True)
        if os.path.exists('/Users/sandeep/Documents/Create__Task/CommunitySettings.csv'):
            os.remove('/Users/sandeep/Documents/Create__Task/CommunitySettings.csv')
        settings.to_csv("CommunitySettings.csv")
    else:
        return -1

def UserCommunity(username):
    user = list(df['Name']).index(username)
    cID = df.loc[int(user)]['CommunityID']
    return(list(df.loc[df['CommunityID'] == cID]['Name']))

def UserCommunityCases(username):
    user = list(df['Name']).index(username)
    cID = df.loc[int(user)]['CommunityID']
    return(scrapeCounty(settings.loc[int(cID)]['County']))

def change_email(username, new_email):
    user = list(df['Name']).index(username)
    #return df.loc[int(user)]['Email']
    df.at[user, 'Email'] = new_email #.replace(to_replace=df.loc[int(user)]['Email'], value = new_email)
    if os.path.exists('/Users/sandeep/Documents/Create__Task/community.csv'):
        os.remove('/Users/sandeep/Documents/Create__Task/community.csv')
    df.to_csv("community.csv")
    return(df.at[user, 'Email'])

if __name__ == "__main__":
    print(change_email('Joe', 'example2@gmail.com'))
#print(settings)