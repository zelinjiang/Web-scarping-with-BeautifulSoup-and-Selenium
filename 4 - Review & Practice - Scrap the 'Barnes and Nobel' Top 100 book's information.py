from bs4 import BeautifulSoup
import requests
import time
from random import randint

## First request: get the link for each of 40 books
url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=40&page=1'
header_my = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

page_bn100 = requests.get(url, headers = header_my)
soup = BeautifulSoup(page_bn100.text, 'lxml')

list_booklinks = []         # this list will contain links of each book
# get a list of the blocks, each block is nested by a book
grand_blocks = soup.find_all('li', class_ = 'pb-s mt-m bd-bottom-disabled-gray record list-view-data')
# iterate over each block and get the link for each book
for grand_block in grand_blocks:
    title_block = grand_block.find('h3', class_ = 'product-info-title')
    link_block = title_block.find('a', href = True)
    link = 'https://www.barnesandnoble.com' + link_block['href']
    list_booklinks.append(link)

# print(list_booklinks)   # for debug use
time.sleep(randint(6,10))


## Second request: visit the link for each book, download each of them
for i in range(40):
    # visit the i_th link, download the page
    link = list_booklinks[i]
    page = requests.get(link, headers = header_my)
    soup = BeautifulSoup(page.content, 'html.parser')
    # write the page into a file
    filename = 'B&N_top100_' + str(i+1) + '.html'
    f = open(filename, 'x')
    f = open(filename, 'w')
    f.write(str(soup))
    f.close()
    time.sleep(randint(6,10))


## open each file, extract the information we need
for i in range(40):
    filename = 'B&N_top100_' + str(i+1) + '.html'
    f = open(filename, "r", encoding = 'utf-8')
    soup = BeautifulSoup(f.read(), 'lxml')

    # Get the book name
    bookname = soup.find('h1', class_ = 'pdp-header-title text-lg-left text-sm-center mr-md-l ml-md-l mr-sm-l ml-sm-l').text
    # Get the old price and new price
    old_new_price_block = soup.find('div', class_ = 'price-current-old-details')
    new_price = old_new_price_block.find('span', class_ = 'price current-price ml-0').text
    try:
        old_price = old_new_price_block.find('s', class_ = 'old-price').text
    except:
        old_price = "Does not exist"

    # Get the first 100 characters of the over view
    overview_block = soup.find('div', class_ = 'bs-content')
    overview = overview_block.text
    overview_100char = overview[0:100]

    print('==================================================')
    print('Book Name:', bookname)
    print('Current Price:', new_price)
    print('Old Price:', old_price)
    print('Overview: ', overview_100char)
    print('\n')


