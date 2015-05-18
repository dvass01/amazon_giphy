import bottlenose
import sys
import xml.etree.cElementTree as ET

class AMZN(bottlenose.Amazon):
    def __init__(self):
        with open('secret_stuff','r') as f:
            lines = f.readlines()
            ASSOCIATE_TAG = lines[1].rstrip()
            ACCESS_KEY_ID = lines[3].rstrip()
            SECRET_ACCESS_KEY = lines[5].rstrip()
        self.url = '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}'
        super().__init__(ACCESS_KEY_ID, SECRET_ACCESS_KEY, ASSOCIATE_TAG)

    def get_first_dvd_result(self, keyword):
        response = self.ItemSearch(Keywords=keyword, SearchIndex="DVD")

        root = ET.fromstring(response.decode())
        item_root = root.find(self.url+'Items')
        ASIN = item_root[4][0]
        return ASIN.text

    def get_image(self, keyword):
        this_ASIN = self.get_first_dvd_result(keyword)
        
        images_response = self.ItemLookup(ItemId=this_ASIN, ResponseGroup='Images')

        images_root = ET.fromstring(images_response.decode())
        images_item_root = images_root.find(self.url+'Items')

        large_image = images_item_root[1][3]

        return large_image.find(self.url+'URL').text

if __name__ == '__main__':
    this_AMZN = AMZN()
    print(this_AMZN.get_image(sys.argv[1]))
