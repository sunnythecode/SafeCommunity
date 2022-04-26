#Scrape.py, webscraping covid case file
from selenium import webdriver # I used the selenium webscraping library
chromedriver = '/Users/sandeep/Downloads/chromedriver 5' #I also used chromedriver with selenium to scrape from a google chrome browser
from functools import reduce
import re



def urlCreate(county): #given a county, create a google search query link for the county covid cases
    pattern = r" "
    new_str = re.sub(pattern, "+", reduce(lambda x, y: x+y, county))
    url = "https://www.google.com/search?q=" + str(new_str) + '+covid+cases'
    return url

def scrapeCounty(County): #Scrape the google covid page for new cases, if shown
    drive = webdriver.Chrome(chromedriver)
    drive = webdriver.chrome.options.Options()
    drive.headless = True
    drive.add_argument('--window-size=1280,1800')
    driver = webdriver.Chrome(executable_path= chromedriver, options= drive)
    query = urlCreate(County)
    driver.get(query)
    try: #If there are new cases, find the HTML element by the xpath for new covid cases
        element = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[3]/div[4]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr/td[1]/div[3]")
    except: #If there are no new cases
        return '0'
    return (element.text)

#End of scraper.py
