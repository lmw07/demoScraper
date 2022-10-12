import json

import listingClass
import requests
from bs4 import BeautifulSoup

#HELPER METHODS
def getNums(string):
    number = int(''.join(filter(str.isdigit, string)))
    return number
#REDFIN METHODS

#SEARCH BY ZIP
def RedfinZipSearch(zipcode):
    listingArr = []
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": f'https://www.redfin.com/zipcode/{zipcode}'}
    response = requests.request('GET', base_url, params=params)
    content = response.text
    soup = BeautifulSoup(content, features='html.parser')
    for element in soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView'}):
        price = element.find('span', attrs={'class': 'homecardV2Price'})
        address = element.find('span', attrs={'class': 'collapsedAddress primaryLine'})
        pic = element.find('img', attrs={'class': 'homecard-image'})
        link = element.find('a', attrs={'class': 'slider-item'})['href']
        if (price and price.text) and (pic) and (address and address.text) and link:
            listing = listingClass.Listing(address, price.text,link,pic)
        listingArr.append(listing)
    res = json.dumps(listingArr)
    return res
