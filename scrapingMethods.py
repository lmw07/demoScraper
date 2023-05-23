'''
import json
import re
import listingClass
import requests
from bs4 import BeautifulSoup

#HELPER METHODS
def getNums(string):
    numberString = (''.join(filter(str.isdigit, string)))
    if len(numberString) > 4:
        firstNum = numberString[0:4]
        secondNum = numberString[4:len(numberString):1]
        return str(firstNum + "-" + secondNum)
    if len(numberString) > 0:
        return int(numberString)
    return "Not Given"
def getRidOfCommas(string):
    resString = string.replace(",","")
    return resString


#REDFIN METHODS

#SEARCH BY ZIP
def RedfinZipSearch(zipcode):
    listingArr = []
    urlHeader = 'https://www.redfin.com'
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": f'https://www.redfin.com/zipcode/{zipcode}/apartments-for-rent'}
    response = requests.request('GET', base_url, params=params)
    if response.status_code == 403:
        return '[]'
    content = response.text
    soup = BeautifulSoup(content, features='html.parser')
    soup = BeautifulSoup(content, features='html.parser')
    elements = soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView isRentals'})
#    elements.append(soup.findAll('div', attrs={'class': 'HomeCardContainer selectedHomeCard defaultSplitMapListView isRentals'})[0])
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
            listing = listingClass.Listing(address.text, getRidOfCommas(price.text), (urlHeader + link), pic)
            listing.setSize(getRidOfCommas(size.text))
            listing.setBedrooms(bedrooms.text)
            listing.setBathrooms(bathrooms.text)
        listingArr.append(listing)
    res = json.dumps(listingArr, default=vars)
    return res

print(RedfinZipSearch(84102))'''






import json
import re
import listingClass
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
#HELPER METHODS
def getNums(string):
    numberString = (''.join(filter(str.isdigit, string)))
    if len(numberString) > 4:
        firstNum = numberString[0:4]
        secondNum = numberString[4:len(numberString):1]
        return str(firstNum + "-" + secondNum)
    if len(numberString) > 0:
        return int(numberString)
    return "Not Given"
def getRidOfCommas(string):
    resString = string.replace(",","")
    return resString


#REDFIN METHODS

#SEARCH BY ZIP
def RedfinZipSearch(zipcode):
    listingArr = []
    urlHeader = 'https://www.redfin.com'
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": f'https://www.redfin.com/zipcode/{zipcode}/apartments-for-rent'}
    response = requests.request('GET', base_url, params=params)
    if response.status_code == 403:
        return '[]'
    content = response.text
    soup = BeautifulSoup(content, features='html.parser')
    soup = BeautifulSoup(content, features='html.parser')
    elements = soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView isRentals'})
#    elements.append(soup.findAll('div', attrs={'class': 'HomeCardContainer selectedHomeCard defaultSplitMapListView isRentals'})[0])
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
            listing = listingClass.Listing(address.text, getRidOfCommas(price.text), (urlHeader + link), pic)
            listing.setSize(getRidOfCommas(size.text))
            listing.setBedrooms(bedrooms.text)
            listing.setBathrooms(bathrooms.text)
        listingArr.append(listing)
    res = json.dumps(listingArr, default=vars)
    return res


def RentlerZipSearch(zipcode):
    #change me
    listingArr = []
    urlHeader = 'https://www.rentler.com'
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": f'https://www.rentler.com/places-for-rent/zip/{zipcode}'}
    response = requests.request('GET', base_url, params=params)
    if response.status_code == 403:
        return '[]'
    content = response.text

    # File path
    #file_path = 'rentlerhtml.txt'

    # Read the file into a string
   # with open(file_path, 'r') as file:
    #    content = file.read()
   # print(content)

    soup = BeautifulSoup(content, features='html.parser')
    elements = soup.findAll('div', attrs={'class': 'listing-item'})

    def parse_element(element):
        price = element.find('h3', attrs={'class': 'price'})
        price = price.contents[0]
        address = element.find('div', attrs={'class': 'address'})
        address = address.contents[0] + address.contents[2]
        stats = element.find('div', attrs={'class': 'bed-bath'})
        bedrooms = stats.contents[0].split('•')[0]
        bathrooms = stats.contents[0].split('•')[1]

  #      temp = element.find('img', attrs={'class': 'image lazyautosizes ls-is-cached lazyloaded'})
        temp = element.find('img', attrs={'class': 'image'})
        pic = temp['data-src']
        link = element.find('a')['href']
        if price and (pic) and address and link:
            listing = listingClass.Listing(address, getRidOfCommas(price), (urlHeader + link), pic)
            listing.setBedrooms(bedrooms)
            listing.setBathrooms(bathrooms)
            return listing
        return None

    # Use multithreading to parse each element in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(parse_element, element) for element in elements]
        for future in as_completed(futures):
            listing = future.result()
            if listing is not None:
                listingArr.append(listing)

    res = json.dumps(listingArr, default=vars)
    print(res)
    return res





RentlerZipSearch(84101)


#print(RedfinZipSearch("84102"))
'''
import json
import re
import listingClass
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

#HELPER METHODS
def getNums(string):
    numberString = (''.join(filter(str.isdigit, string)))
    if len(numberString) > 4:
        firstNum = numberString[0:4]
        secondNum = numberString[4:len(numberString):1]
        return str(firstNum + "-" + secondNum)
    if len(numberString) > 0:
        return int(numberString)
    return "Not Given"

def getRidOfCommas(string):
    resString = string.replace(",","")
    return resString


#REDFIN METHODS

#SEARCH BY ZIP
def RedfinZipSearch(zipcode):
    listingArr = []
    urlHeader = 'https://www.redfin.com'
    base_url = 'https://api.webscrapingapi.com/v1'
    params = {"api_key": "Jbdkg6N2W1QEtw2JFs84CmfCeOozu4Nj",
              "url": f'https://www.redfin.com/zipcode/{zipcode}/apartments-for-rent'}
    response = requests.request('GET', base_url, params=params)
    if response.status_code == 403:
        return '[]'
    content = response.text
    soup = BeautifulSoup(content, features='html.parser')
    soup = BeautifulSoup(content, features='html.parser')
    elements = soup.findAll('div', attrs={'class': 'HomeCardContainer defaultSplitMapListView isRentals'})

    # Define a function to parse each element in parallel
    def parse_element(element):
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
            listing = listingClass.Listing(address.text, getRidOfCommas(price.text), (urlHeader + link), pic)
            listing.setSize(getRidOfCommas(size.text))
            listing.setBedrooms(bedrooms.text)
            listing.setBathrooms(bathrooms.text)
            return listing
        return None

    # Use multithreading to parse each element in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(parse_element, element) for element in elements]
        for future in as_completed(futures):
            listing = future.result()
            if listing is not None:
                listingArr.append(listing)

    res = json.dumps(listingArr, default=vars)
    return res

'''