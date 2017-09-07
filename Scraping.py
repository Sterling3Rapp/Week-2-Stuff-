import requests
import bs4

r = requests.get ("http://www.ccgov.org/government/sheriff-s-office-1701")
#print(r.content)

soup = bs4.BeautifulSoup(r._content,'html.parser')

#print(soup)
print(soup.title)
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

