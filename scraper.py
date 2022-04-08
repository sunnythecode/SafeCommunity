from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.common.keys import Keys
import os
import time
chromedriver = '/Users/sandeep/Downloads/chromedriver 5'

def scrapeCounty(County):
    drive = webdriver.Chrome(chromedriver)
    drive = webdriver.chrome.options.Options()
    drive.headless = True
    drive.add_argument('--window-size=1280,1800')
    driver = webdriver.Chrome(executable_path= chromedriver, options= drive)
    countyIN = County.split()
    query = ""
    for i in countyIN:
        query = query + i + '+'
    query = query[:-1] + '+covid'
    driver.get('https://www.google.com/search?q='+ query + '&safe=active&ssui=on')
    return(driver.find_element_by_class_name('h5Hgwe').text)
if __name__ == "__main__":
    print(scrapeCounty('Los Angeles County'))
#print(settings)