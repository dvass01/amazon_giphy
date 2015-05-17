import bottlenose
import sys
import xml.etree.cElementTree as ET

def whole_thing_as_a_function(keyword):
    ASSOCIATE_TAG = 'gipvsama-20'
    ACCESS_KEY_ID = 'AKIAIARB46MNH2PWDECA'
    SECRET_ACCESS_KEY='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'

    amazon = bottlenose.Amazon(ACCESS_KEY_ID, SECRET_ACCESS_KEY, ASSOCIATE_TAG)
    url = '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}'

    response = amazon.ItemSearch(Keywords=keyword, SearchIndex="DVD")

    root = ET.fromstring(response.decode())
    item_root = root.find(url+'Items')
    #item_ASIN = item_list.find(url+'ASIN')
    ASIN = item_root[4][0]

    images_response = amazon.ItemLookup(ItemId=ASIN.text, ResponseGroup='Images')

    images_root = ET.fromstring(images_response.decode())
    images_item_root = images_root.find(url+'Items')

    large_image = images_item_root[1][3]

    return large_image.find(url+'URL').text

if __name__ == '__main__':
    print(whole_thing_as_a_function(sys.argv[1]))
