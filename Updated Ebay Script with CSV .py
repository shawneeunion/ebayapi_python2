#Part 0: Leading the Packages 
###
pip ebaysdk
from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

#Part 1: Connecting to the eBay Platform. You will need to obtain a ID_APP from ebay developers website. https://developer.ebay.com/
ID_APP = 'INSERT_YOUR_ID'
api = finding(https=True, appid=ID_APP, config_file=None)
response = api.execute('findCompletedItems', { 'keywords': 'Nikon FM' }, {'categoryId':'15230'})

#Part 2: Using Beautiful Soup to parse the content. 
soup = BeautifulSoup(response.content,'lxml')
items = soup.find_all('item')

#Part 3: Writing your pull to a CSV file 

import csv
table = items

f = csv.writer(open("nikonfm.csv",'w'))
f.writerow(["title","price","outcome","soldtime"])

for item in items: 
    title       = item.title.get_text()
    price       = item.currentprice.get_text() 
    outcome     = item.sellingstate.get_text()
    soldtime    = item.endtime.get_text()
    f.writerow([title,price,outcome,soldtime])