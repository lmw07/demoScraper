import json

import listingClass
import requests
from bs4 import BeautifulSoup

#HELPER METHODS
def getNums(string):
    numberString = (''.join(filter(str.isdigit, string)))
    if len(numberString) > 0:
        return int(numberString)
    return "Not Given"
#REDFIN METHODS

#SEARCH BY ZIP
def RedfinZipSearch(zipcode):
    listingArr = []
    urlHeader = 'https://www.redfin.com'
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": f'https://www.redfin.com/zipcode/{zipcode}/apartments-for-rent'}
    response = requests.request('GET', base_url, params=params)
    content = response.text
    soup = BeautifulSoup(content, features='html.parser')
    soup = BeautifulSoup(content, features='html.parser')
    if response.status_code == 200:
        elements = soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView isRentals'})
    elements.append(soup.findAll('div', attrs={'class': 'HomeCardContainer selectedHomeCard defaultSplitMapListView isRentals'})[0])
    for element in elements:
        price = element.find('span', attrs={'class': 'homecardV2Price'})
        address = element.find('span', attrs={'class': 'fullAddress'})
        if not element.find('span', attrs={'class': 'fullAddress'}):
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
    res = json.dumps(listingArr, default=vars)
    return res

print(RedfinZipSearch(84102))