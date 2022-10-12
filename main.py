# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import listingClass
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
import json
def getNums(string):
    numberString = (''.join(filter(str.isdigit, string)))
    if len(numberString) > 0:
        return int(numberString)
    return "Not Given"
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
    listingArr = []
    driver.get('https://www.redfin.com/zipcode/84102')

    urlHeader = 'https://www.redfin.com'
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')
    for element in soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView'}):
        price = element.find('span', attrs={'class': 'homecardV2Price'})
        address = element.find('span', attrs={'class': 'collapsedAddress primaryLine'})
        stats = element.find('div', attrs={'class': 'HomeStatsV2 font-size-small'})
        bedrooms = stats.contents[0]
        bathrooms = stats.contents[1]
        size = stats.contents[2]
        temp = element.find('img', attrs={'class': 'homecard-image'})
        if len(temp["class"]) == 1:
            pic = temp['src']
        else:
            pic = temp['data-src']
        link = element.find('a', attrs={'class': 'slider-item'})['href']
        if (price and price.text) and (pic) and (address and address.text) and link:
            listing = listingClass.Listing(address.text, getNums(price.text), (urlHeader + link), pic)
            listing.setSize(getNums(size.text))
            listing.setBedrooms(getNums(bedrooms.text))
            listing.setBathrooms(getNums(bathrooms.text))
        listingArr.append(listing)
    driver.quit()
    with open("redfinListings.json", "w") as write_file:
        json.dump(listingArr, write_file, default=vars)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
redfin()
