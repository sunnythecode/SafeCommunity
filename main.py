#python -m pip install beautifulsoup4
import csv
import re
from datetime import date, timedelta
from functools import reduce
import math
from bs4 import BeautifulSoup
import pandas as pd
import requests
from dbhelper import *

f = open('StateSaver.txt', 'r')
contents= f.read()
print("Your State Is Currently: " + str(contents))
stateG = str(contents)



 
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
            return 1
        else:
            print("Incorrect Login Information")
            login()
    else: 
        print('please type yes or no')
        


def Dashboard():
    print("Dash")
    return 1

def Community_View():
    print("Community_View")

login_value = login()
if login_value == 1:
    dash_value = Dashboard()
    if dash_value == 1:
        comm = Community_View()

def getDateAndFormat(backDays):
  today = date.today()
  today = str(today - timedelta(days=backDays))
  formmattedDate = today[-5] + today[-4] + '-' + today[-2] + today[-1] + '-' + today[0:4]
  return(formmattedDate)

today = getDateAndFormat(1)
yesterday = getDateAndFormat(2)


def scrape(formmattedDate):
#Uses a public dataset for information on COVID cases based in states. Dataset is updated at the end of every day. The link will take you to the raw data, which is fetched by webscraping the html.
    response = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + formmattedDate+ '.csv')


    soup = BeautifulSoup(response.content, 'html.parser')
    return str(soup)



TodayRes = scrape(today)
YesterdayRes = scrape(yesterday)

def sort(res):
  newList = []
  statesList = []
  for i in range(len(res)):
    newList.append(res[i])
  tempList = []

  for item in newList:
    if item == "\n":
      statesList.append(reduce(lambda x, y: x+y, tempList))
      tempList=[]
    else:
      tempList.append(item)

  statesList.remove(statesList[0])
  newStatesList = []
  for item in statesList:
    newStatesList.append(item.split(","))
  return newStatesList
  

todaysInfo = sort(TodayRes)
yesterdaysInfo = sort(YesterdayRes)

def findState(state, formattedRes):
  for item in formattedRes:
    if item[0] == state:
      foundState = (item)
      break
  return foundState

stateInfo = findState(stateG, todaysInfo)
yesterStateInfo = findState(stateG, yesterdaysInfo)

def getCountry(state):
  if state[1] != "":
    return state[1]
  else:
    return "Not Available"

def getLat(state):
  if state[3] != "":
    return state[3]
  else:
    return "Not Available"

def getLong(state):
  if state[4] != "":
    return state[4]
  else:
    return "Not Available"

def getConfirmedCases(state):
  if state[5] != "":
    return state[5]
  else:
    return "Not Available"

def getDeaths(state):
  if state[6] != "":
    return state[6]
  else:
    return "Not Available"



def dailySummary(state, yesterState):
  print()
  print("There have been a total of " + str(getDeaths(state)) + " deaths in your state of " + str(state[0]).upper() + ".")
  print()
  print("There have been a total of " + str(getConfirmedCases(state)) + " confirmed cases in your state of " + str(state[0]).upper() + ".")
  print()
  print("There have been a total of " + str(int(getDeaths(state)) - int(getDeaths(yesterState))) + " deaths TODAY in your state of " + str(state[0]).upper() + ".")
  print()
  print("There have been a total of " + str(int(getConfirmedCases(state)) - int(getConfirmedCases(yesterState))) + " confirmed cases TODAY in your state of " + str(state[0]).upper() + ".")

dailySummary(stateInfo, yesterStateInfo)

def changeState():
  print("What is your state? (ex Arizona)")
  x = input()
  global stateG 
  stateG = str(x)

changeState()

#Must be last in order to correctly save the state of the user.
file1 = open("StateSaver.txt", "w") 
str1 = str(stateG)
file1.write(str1)
file1.close()