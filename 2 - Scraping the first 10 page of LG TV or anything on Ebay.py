from bs4 import BeautifulSoup
import requests
import time
from random import randint

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

# Get the number of items are found in the search result
# By default each page shows 50 items,
# so if more than 500 items are found, then we need to scrape 10 pages
# if less than 500 items are found, then we need to scrape (num_items // 50 + 1) pages
url = "https://www.ebay.com/sch/i.html?_nkw=lg+tv"
page = requests.get(url, user_agent)
soup = BeautifulSoup(page.text, 'lxml')
result_num_block = soup.find('h1', class_ = 'srp-controls__count-heading')
result_num = int(result_num_block.find('span', class_ = 'BOLD').text)

# if the search result contains more than 500 items -> scrape 10 pages
if result_num >= 500:
    for i in range(10):
        url = "https://www.ebay.com/sch/i.html?_nkw=lg+tv&_pgn=" + str(i+1)
        # create the file to save the html document
        file_name = "ebay_lg_tv_page"+str(i+1)+".html"
        f = open(file_name, "x")
        # write the page into the file created
        f = open(file_name, "w")  # open the file to write the file
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        f.write(str(soup))  # write the page into a html file
        f.close()

        # request a page for every 20 seconds
        time.sleep(randint(18, 24))
# if the search result contains less than 500 items -> scrape [(result_num // 50) + 1] pages
else:
    # calculate the number of page needs to scrape
    scrape_page_num = (result_num // 50) + 1
    for i in range(scrape_page_num):
        url = "https://www.ebay.com/sch/i.html?_nkw=lg+tv&_pgn=" + str(i+1)
        # create the file to save the html document
        file_name = "ebay_lg_tv_page"+str(i+1)+".html"
        f = open(file_name, "x")
        # write the page into the file created
        f = open(file_name, "w")  # open the file to write the file
        page = requests.get(url, user_agent)
        soup = BeautifulSoup(page.content, 'html.parser')
        f.write(str(soup))  # write the page into a html file
        f.close()

        time.sleep(randint(18, 24))


# outer for loop: open 10 html files on by one
for i in range(10):
    open_file_name =  "ebay_lg_tv_page"+str(i+1)+".html"
    f = open(open_file_name, "r", encoding = 'utf-8')
    soup = BeautifulSoup(f.read(), 'lxml')
    item_blocks = soup.find_all('div', class_ = "s-item__wrapper clearfix")

    # inner for loop: within each html file, check each item one by one
    for items in item_blocks:
        try:
            sponsor_block0 = items.find('div', class_ = 's-item__info clearfix')
            sponsor_block1 = sponsor_block0.find('div', class_ = "s-item__details clearfix")
            sponsor_block2 = sponsor_block1.find_all('div', class_ = 's-item__detail s-item__detail--primary')
            sponsor_block3 = sponsor_block2[-1].find('span', class_ = 's-item__sep')
            sponsor_block4 = sponsor_block3.span.find_all('span')

            link = sponsor_block0.find('a', href = True)
            print(link['href'], '\n')

        except:
            continue






    
