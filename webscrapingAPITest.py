# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import json
import requests


def rentler():
    listings = []
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key":"JBRtIH5Jk4GGhksdLEFlahaY4M3iWzEt", "url": 'https://www.rentler.com/places-for-rent/zip/84102/'}
    response = requests.request('GET', base_url, params=params)
    content=response.text
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


def redfin():
    listings = []
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": 'https://www.redfin.com/zipcode/84101', "timeout": "15000"}
    response = requests.request('GET', base_url, params=params)
    content = response.text
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

def pythonAnywhere(zipcode):
    baseUrl = 'http://lm07.pythonanywhere.com/'
    response = requests.request('GET', baseUrl)
    print(response.text)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#redfin()
pythonAnywhere(64801)
