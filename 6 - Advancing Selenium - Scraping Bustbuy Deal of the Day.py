from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from datetime import date

# Get the date and time of scrapping
now = datetime.now()
now_format = now.strftime("%d/%m/%Y %H:%M:%S")

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(10)
driver.set_script_timeout(200)
driver.set_page_load_timeout(40)

### Go to Bestbuy.com
driver.get('https://www.bestbuy.com/')

time.sleep(5.2)

### if there is a pop-up window tell us to subscribe deal information, close it
try:
    pop_window = driver.find_element_by_xpath("//button[@class='c-close-icon c-modal-close-icon']")
    pop_window.click()
    time.sleep(5)
except:
    pass


### Click 'Deal of the Day' button on the top bar
dealoftheday = driver.find_element_by_xpath("//a[text()='Deal of the Day']")
dealoftheday.click()
time.sleep(3)

### Get the time left
timeleftbox = driver.find_element_by_css_selector("span[data-testid='expiration-message']")
timeleft = timeleftbox.text
print("Current Time:{}\n{}".format(now_format, timeleft))


### Click on the 'Deal of the Day' item
first_item = driver.find_element_by_css_selector("a[class='wf-offer-link v-line-clamp ']")
first_item.click()
time.sleep(6)

### Scroll down to load the Review section (Maybe not necessary)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.5)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.8)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.4)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.3)


### Click on 'Review' of the Deal of the Day item
review_button = driver.find_element_by_css_selector("span[class='d-flex align-items-center']")
review_button.click()
time.sleep(2)

### Creat a file and save the page
file_name = 'bestbuy_deal_of_the_day.htm'
f = open(file_name, "x")
# Write the page into the file created
f = open(file_name, "w")  # open the file to write the file
page = driver.page_source
f.write(page)
f.close()

time.sleep(10)
driver.quit()

# We have printed the 'Time Left' earlier, but it is embedded in the working-log in the console
# So here we print it again just for clearity
print("\n===============================================================")
print("Check Time: {}\n{}".format(now_format, timeleft))


### Using Selenium to get the next sibling
# from selenium import webdriver
# driver = webdriver.Chrome()

# driver.get('https://140f670e-5774-43b5-a1a5-c993f66fa51d.htmlpasta.com/')

# element = driver.find_element_by_xpath("//*[contains(text(), 'Open Until')]")
# prevSibling = element.find_element_by_xpath('.//preceding-sibling::*')
# nextSibling = element.find_element_by_xpath('.//following-sibling::*')

# print(prevSibling.tag_name + ': ' + prevSibling.text)
# print(element.tag_name + ': ' + element.text)
# print(nextSibling.tag_name + ': ' + nextSibling.text)
# driver.close()
