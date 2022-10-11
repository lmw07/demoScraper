import requests
from bs4 import BeautifulSoup
import json

MAX_THREADS = 30
BASE_URL = "https://www.redfin.com/zipcode/84102"
listings = []
resp = requests.get(BASE_URL)
soup = BeautifulSoup(resp.content, "html.parser")
'''
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

'''
img_data = requests.get('https://photos.zillowstatic.com/fp/9fcbc31769aa3a9f02ec66403e48a252-p_e.jpg').content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

