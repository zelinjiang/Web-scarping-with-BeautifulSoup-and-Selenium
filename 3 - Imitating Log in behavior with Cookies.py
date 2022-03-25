from bs4 import BeautifulSoup
import requests
import time

url_login = 'https://www.planespotters.net/user/login'
header_my = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}


### First request: get the cookies the server gives the browser before login
session_getcookies = requests.session()
res1 = session_getcookies.get(url_login, headers = header_my)
# get the cookies server send to browser before login
cookies_beforelogin = session_getcookies.cookies.get_dict()
# print("cookies before login:")  # for debug use
# print(cookies_beforelogin)      # for debug use
time.sleep(10)


### Second request: get the hidden "csrf" that will be also submitted while logging in
# find the form that we input the username, password and submit
page_login = requests.get(url_login, headers = header_my, cookies = cookies_beforelogin)
soup = BeautifulSoup(page_login.text, 'lxml')
form = soup.find('div', class_ = 'planespotters-form')
# get the hidden "csrf"
csrf_my = form.find(id = 'csrf').get('value')
# print('csrf:')     # for debug use
# print(csrf_my)     # for debug use
time.sleep(10)


### Third request: Login and get the cookies after login
session_login = requests.session()

res2 = session_login.post(url_login,
    headers = header_my,
    cookies = cookies_beforelogin,
    data = {'username' : 'jzl123456@gmail.com',  # write your username
            'password' : 'jzl123456',            # write your password
            'csrf' : csrf_my,
            'rid': ''},
    timeout = 10)
time.sleep(10)

# get the cookies the server sent after logged in
cookies_afterlogin = session_login.cookies.get_dict()
# print("cookies after login:")     # for debug use
# print(cookies_afterlogin)         # for debug use

# combine the cookies get before login and after login
cookies = {**cookies_beforelogin, **cookies_afterlogin}
# print('cookies combined')         # for debug use
# print(cookies)                    # for debug use


# get the profile page after login
page_logged = session_login.get('https://www.planespotters.net/member/profile',
                                headers = header_my, cookies = cookies)
page_logged_soup = BeautifulSoup(page_logged.content, 'html.parser')
# Check if my username exists in the profile page
name_exist = bool(page_logged_soup.findAll(text = 'ZelinJustin'))


print("Profile page after login: ")
print(page_logged_soup.prettify())
print("=========================================================\n")
print("Combined Cookies: ")
print(cookies)
print("=========================================================\n")
print("Name exist in profile page? ")
print(name_exist)
