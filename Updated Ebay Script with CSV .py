from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

ID_APP = 'INSERT_YOUR_ID'

api = finding(https=True, appid=ID_APP, config_file=None)
#response = api.execute('findCompletedItems', { 'keywords': 'Nikon FM' })
response = api.execute('findCompletedItems', { 'keywords': 'Nikon FM' }, {'categoryId':'15230'})


soup = BeautifulSoup(response.content,'lxml')
#totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

#Creating the CSV file 

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