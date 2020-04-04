import bs4
import requests

r=requests.get("http://books.toscrape.com/")

soup=bs4.BeautifulSoup(r.text, "lxml")

print(soup) #parse everything
print(soup.find('h3')) #parse the first h3 elemnt
print(soup.find_all('h3')) #parse all h3 selemnt

booktitles = soup.find_all('h3') #loop over every booktitle
for booktitle in booktitles:
    print(booktitle.text)

booklinks = soup.find_all('h3') #Loop over every booklink
for booklink in booklinks:
    print('http://books.toscrape.com/' +str(booktitle.find('a')['href']))

linkList = [] #print all results in a list
for booklink in booklinks:
    linkList.append('http://books.toscrape.com/' +str(booktitle.find('a')['href']))
