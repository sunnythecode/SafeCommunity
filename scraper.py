#Scrape code for covid cases
#python -m pip install beautifulsoup4

rom datetime import date, timedelta
from functools import reduce
import math
from bs4 import BeautifulSoup
today = date.today()

today = str(today - timedelta(days=1))
print(today)
formmattedDate = today[-5] + today[-4] + '-' + today[-2] + today[-1] + '-' + today[0:4]
print(formmattedDate)

def scrape():
#Uses a public dataset for information on COVID cases based in states. Dataset is updated at the end of every day. The link will take you to the raw data, which is fetched by webscraping the html.
    response = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + formmattedDate+ '.csv')
    soup = BeautifulSoup(response.content, 'html.parser')
    return str(soup).split()
