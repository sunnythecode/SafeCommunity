from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.common.keys import Keys
import os
import time
chromedriver = '/Users/sandeep/Downloads/chromedriver 5'
from functools import reduce
import re



def urlCreate(county):
    pattern = r" "
    new_str = re.sub(pattern, "+", reduce(lambda x, y: x+y, county))
    url = "https://www.google.com/search?q=" + str(new_str) + '+covid+cases'
    return url

def scrapeCounty(County):
    drive = webdriver.Chrome(chromedriver)
    drive = webdriver.chrome.options.Options()
    drive.headless = True
    drive.add_argument('--window-size=1280,1800')
    driver = webdriver.Chrome(executable_path= chromedriver, options= drive)
    query = urlCreate(County)
    driver.get(query)
    driver.save_screenshot('/Users/sandeep/Documents/Create__Task/SCRAPE.png')
    #return(driver.find_element_by_class_name('h5Hgwe'))
    try:
        element = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[3]/div[4]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr/td[1]/div[3]")
    except:
        return '0'
    return (element.text)
if __name__ == "__main__":
    print(scrapeCounty('Santa Clara county'))
#print(settings)