from datetime import date, timedelta
from functools import reduce
from bs4 import BeautifulSoup
import requests


def getDateAndFormat(backDays):
  today = date.today()
  today = str(today - timedelta(days=backDays))
  formmattedDate = today[-5] + today[-4] + '-' + today[-2] + today[-1] + '-' + today[0:4]
  #formats the date in a way the url accepts
  return(formmattedDate)
  
def scrapeState(formmattedDate):
#Uses a public dataset for information on COVID cases based in states. Dataset is updated at the end of every day. The link will take you to the raw data, which is fetched by webscraping the html.
    response = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + formmattedDate+ '.csv')


    soup = BeautifulSoup(response.content, 'html.parser') #Gets the data needed from the link using beautifulSoup4, a common webscraping library
    return str(soup)

def arrange(res):
  newList = []
  statesList = []
  tempList = []
  
  for i in range(len(res)):
    newList.append(res[i])
    
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
  #Formats the lis in format [STATE NAME, COUNTRY, LAT, LONG, CASES, DEATHS, etc] for all states, returns a list of statesLists 

def findState(state, formattedRes):
  for item in formattedRes:
    if item[0] == state:
      foundState = (item)
      break
  return foundState
  
#Selection is demonstrated here. I am selecting a certain state from a list of all states. I am doing this by iterating through a list and selecting the array within the list of list whose first position matches that of the inputted state.

  
def getCountry(state):
  if state[1] != "":
    return state[1]
  else:
    return "Not Available"
    #Gets the country by using selection

def getConfirmedCases(state):
  if state[5] != "":
    return state[5]
  else:
    return "Not Available"
    #Gets the cases by using selection

def getDeaths(state):
  if state[6] != "":
    return state[6]
  else:
    return "Not Available"
    #Gets the deaths by using selection

def dailySummary(state, yesterState):
  print()
  print("There have been a total of " + str(getDeaths(state)) + " deaths in your state of " + str(state[0]).upper() + ".")
  print()
  print("There have been a total of " + str(getConfirmedCases(state)) + " confirmed cases in your state of " + str(state[0]).upper() + ".")
  print()
  print("There have been a total of " + str(int(getDeaths(state)) - int(getDeaths(yesterState))) + " deaths TODAY in your state of " + str(state[0]).upper() + ".")
  print()

#Prints wanted information



