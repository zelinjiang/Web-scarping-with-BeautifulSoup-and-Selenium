from bs4 import BeautifulSoup
import requests
# import the date time library to get the current date of scrapping, in case we need to log the historical price
from datetime import datetime

# Get the date and time of scrapping
now = datetime.now()
now_format = now.strftime("%d/%m/%Y %H:%M:%S")

# For rubostness, build a function to check if there is old price exists for the first spotlight deal item;
# If there is a old price, return the old price;
# If there isn't a strike-trhough price, A.K.A., old price, return False
def test_old_price():
    try:
        dne_summary_card_wrapper = soup.find('div', class_ = 'ebayui-dne-summary-card__wrapper')
        div_1 = dne_summary_card_wrapper.find('div', class_ = 'dne-itemtile dne-itemtile-xlarge')
        div_2 = div_1.find('div', class_ = 'dne-itemtile-detail')
        div_3 = div_2.find('div', class_ = 'dne-itemtile-original-price')
        old_price = div_3.find('span', class_ = 'itemtile-price-strikethrough').text
        return old_price
    except:
        return False

# Create a object of the page that we need to scrape
url= " https://www.ebay.com/deals"
page = requests.get(url)
# Create a beautifulsoup object from the page object, parse the file with the lxml protocol
soup = BeautifulSoup(page.text, 'lxml')

# Get the name of the first spotlight deal item
spotlight_deal = soup.find('h3', class_ = 'dne-itemtile-title ellipse-3').span.text
# Get the reduced price of the first spotlight deal item
reduced_price = soup.find('div', class_ = 'dne-itemtile-price').span.text
# Call the test_old_price function; get the old price if there is one; get False if there isn't old price
old_price = test_old_price()

# If old price doesn't exist, print this version
if (old_price == False):
    print("The first spotlight deal at {} is '{}'; the current price is {}; the price for this item has not been reduced.".format(now_format, spotlight_deal, reduced_price))
#If old price exists, print this version
else:
    print("The first spotlight deal at {} is '{}'; the reduced price is {}; the old price is {}.".format(now_format, spotlight_deal, reduced_price, old_price))
