from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(10)
driver.set_script_timeout(120)
driver.set_page_load_timeout(10)

### Go to Google.com
driver.get('https://www.google.com')

# Switch to English website of Google.com
# because my system language is Chinese so google always load the chinese website by default
# I used a try-except clause so that if your browser automatically load the English version, nothing will happen
try:
    english_website = driver.find_element_by_xpath("//a[text()='English']")
    english_website.click()
except:
    pass

time.sleep(7)

### Search for 'askew'
searchbar = driver.find_element_by_css_selector("input[title='Search']")
searchbar.send_keys('askew\n')
# The whole page became skewed and I thought my computer was broken
time.sleep(10)

### Search for 'Google in 1998'
# firstly clear the search bar, otherwise the new search term will be contated with the search term for last time
clear_inputbox = driver.find_element_by_css_selector("path[d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z']")
clear_inputbox.click()
# input the search term
searchbar = driver.find_element_by_css_selector("input[aria-label='Search']")
searchbar.send_keys('google in 1998\n')
# This is how Google looks like when I was born!
time.sleep(10)
driver.quit()


