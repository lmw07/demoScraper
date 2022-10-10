# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def rentler():
    driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
    prices = []
    addresses = []
    driver.get('https://www.rentler.com/places-for-rent/zip/84102/')

    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')
    for element in soup.findAll('div', attrs={'class': 'col-12 col-lg-6'}):
        price = element.find('h3', attrs={'class': 'price'})
        address = element.find('div', attrs={'class': 'address'})

        if price and price.text:
            prices.append(price.text)
        else:
            prices.append('No display data')

        if address and address.text:
            addresses.append(address.text)
        else:
            addresses.append('No display data')
    df = pd.DataFrame({'Address': addresses, 'Price': prices})
    df.to_csv('rentlerListings.csv', index=False, encoding='utf-8')


def redfin():
    driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
    prices = []
    addresses = []
    driver.get('https://www.redfin.com/zipcode/84102')

    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')
    for element in soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView'}):
        price = element.find('span', attrs={'class': 'homecardV2Price'})
        address = element.find('span', attrs={'class': 'collapsedAddress primaryLine'})

        if price and price.text:
            prices.append(price.text)
        else:
            prices.append('No display data')

        if address and address.text:
            addresses.append(address.text)
        else:
            addresses.append('No display data')
    df = pd.DataFrame({'Address': addresses, 'Price': prices})
    df.to_csv('redfinListings.csv', index=False, encoding='utf-8')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
redfin()