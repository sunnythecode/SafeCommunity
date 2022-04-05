
import pandas as pd
import os
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

if __name__ == "__main__":
    print(isUser("Joe", "pass"))
#print(settings)