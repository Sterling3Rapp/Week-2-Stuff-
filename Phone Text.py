import requests
import bs4
import re

r = requests.get("http://www.delawareonline.com")

soup=bs4.BeautifulSoup(r.content,'html.parser')
phoneNumberPattern = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
s = str(soup)
resultObject = phoneNumberPattern.search(s)
try:
    print("Phone number(s) found: ",resultObject.group())
except:
    print("No phone number found")
'''
print(soup.title)
links =soup.find_all('a')
for link in links:
    print(link.get('href'))
'''