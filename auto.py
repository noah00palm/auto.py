import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# * Automate File, Folder, and Terminal Interactions
# ? How to read files
# f = open('inputFile.txt', 'r') # The 'r' means you want to read data
# print(f.read())
# f.close() # It's best practice to close a file

# ? How to write files
# f = open('inputFile.txt', 'r')
# passFile = open('passFile.txt', 'w') # The 'w' means you want to write data
# failFile = open('failFile.txt', 'w')
# for line in f:
#     line_split = line.split()  # The split() method splits a string into a list
#     if line_split[2] == 'P':
#         passFile.write(line)
#     else:
#         failFile.write(line)
# f.close()
# passFile.close()
# failFile.close()

# * Web Scraping with Beautiful Soup
# ? Creating a request and parsing
# # Make sure requests and BeautifulSoup are imported
# # You can store the site you want to scrape inside a variable
# url = 'http://quotes.toscrape.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html')  # If lxml doesn't work use 'html'
# print(soup.prettify())

# Exploring HTML structure

# ? How to isolate data
# # Make sure requests and BeautifulSoup are imported
# url = 'http://quotes.toscrape.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print(authors[i].text + '\n')

# ? Preparing for paginated scraping
# # Make sure requests and BeautifulSoup are imported
# url = 'https://scrapingclub.com/exercise/list_basic/page=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html')
# count = 1
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# for i in items:
#     itemName = i.find('h4', class_='card-title').text
#     itemPrice = i.find('h5').text
#     print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
#     count = count + 1

# ? Scraping paginated content
# # Make sure requests and BeautifulSoup are imported
# url = 'https://scrapingclub.com/exercise/list_basic/page=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html')
# count = 1
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# for i in items:
#     itemName = i.find('h4', class_='card-title').text
#     itemPrice = i.find('h5').text
#     print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
#     count = count + 1
# pages = soup.find('ul', class_='pagination')
# urls = []
# links = pages.find_all('a', class_='page-link')
# for link in links:
#     pageNum = int(link.text) if link.text.isdigit() else None
#     if pageNum != None:
#         x = link.get('href')
#         urls.append(x)
# print(urls)
# count = 1
# for i in urls:
#     newUrl = url + i
#     response = requests.get(newUrl)
#     soup = BeautifulSoup(response.text, 'html')
#     items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#     for i in items:
#         itemName = i.find('h4', class_='card-title').text
#         itemPrice = i.find('h5').text
#         print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
#         count = count + 1
