# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
import json


def rentler():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
    listings = []
    driver.get('https://www.rentler.com/places-for-rent/zip/84102/')

    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')
    for element in soup.findAll('div', attrs={'class': 'col-12 col-lg-6'}):
        listing = []
        price = element.find('h3', attrs={'class': 'price'})
        address = element.find('div', attrs={'class': 'address'})

        if price and price.text:
            listing.append(price.text)
        else:
            listing.append('No display data')

        if address and address.text:
            listing.append(address.text)
        else:
            listing.append('No display data')
        listings.append(listing)
    with open("rentlerListings.json", "w") as write_file:
        json.dump(listings, write_file)
    driver.quit()


def redfin():
    driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
    listings = []
    driver.get('https://www.redfin.com/zipcode/84102')

    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')
    for element in soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView'}):
        price = element.find('span', attrs={'class': 'homecardV2Price'})
        address = element.find('span', attrs={'class': 'collapsedAddress primaryLine'})
        listing = []
        if price and price.text:
            listing.append(price.text)
        else:
            listing.append('No display data')

        if address and address.text:
            listing.append(address.text)
        else:
            listing.append('No display data')
        listings.append(listing)
    with open("redfinListings.json", "w") as write_file:
        json.dump(listings, write_file)
    driver.quit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
redfin()
