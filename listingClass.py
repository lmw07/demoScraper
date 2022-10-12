class Listing:
    def __init__(self, address, price, link, pic):
        self.address = address
        self.price = price
        self.link = link
        self.pic = pic
        self.bedrooms = 'undefined'
        self.size = 'undefined'
        self.bathrooms = 'undefined'

    def setBedrooms(self, bedrooms):
        self.bedrooms = bedrooms

    def setBathrooms(self, bathrooms):
        self.bathrooms = bathrooms

    def setSize(self, size):
        self.size = size
