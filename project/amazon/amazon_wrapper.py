import bottlenose
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter()

ASSOCIATE_TAG = 'gipvsama-20'
ACCESS_KEY_ID = 'AKIAIARB46MNH2PWDECA'
SECRET_ACCESS_KEY='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'

amazon = bottlenose.Amazon(ACCESS_KEY_ID, SECRET_ACCESS_KEY, ASSOCIATE_TAG)

response = amazon.ItemSearch(Keywords=sys.argv[1], SearchIndex="All")

pp.pprint(response.decode())
