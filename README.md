# Web-scarping-with-BeautifulSoup-and-Selenium

Hey there, welcome to Zelin's Master of Science in Web-scraping (MSWS) program.😂

This repo consists of 6 web-scraping exercises that will free your hand and save your time on getting any information from any webpage. After finishing these 6 step-by-step exercise, you will be able to scrape comments and do your NLP research, you will be also able to scrape your competitor's price information to strategically pricing your products, you can even use it to integrate information from multiple source and build your own business! Don't worry if you don't know any thing about web-scraping yet, there is also where I started from. 

In the first 4 practices, we will mainly use two Python packages: 
- One is the 'requests' package, which is able to access any webpage and store the page into an object.          
- Another one is called 'BeautifulSoup'🥣, which can help you parse the webpage object so that you can locate the block that your focal information lies in, and then extract it.         
It is highly recommended that you keep the BeautifulSoup official documentation by your hand: https://beautiful-soup-4.readthedocs.io/en/latest/. Remember, like all programming puzzles, there is no single solution for any task, read through the documentation and try to customize my code into your own way!          

In the 5th and 6th practice, we will introduce how to deal with some webpages that are dynamically changing, for example, sometimes you may find that you need to scroll down to load more information (like LinkedIn, Instagram, etc), instead of clicking the page numbers. In this case, it is not possible to load more information by editing the variables embedded in the url link (e.g.: pgn=2 for second page).
In this case, there is a powerful package called 'Selenium' that can automate your browser to imitate human behaviors, e.g.: scroll down, click links, etc

## Here are the problems that my code is solving: 

### 1 - Scraping the Ebay 'Spotlight Deal' of each day:
- (1) Write a code to access the url - https://www.ebay.com/deals. 
- (2) Find the first “Spotlight deal” on the website.
- (3) Return/print the old and reduced price of the same. (For example, the first spotlight deal is for the product let’s say, Acer Chromebook. The original price was $249.99, and the new reduced deal price is $129.99.)

### 2 - Scraping the first 10 page of LG TV or anything on Ebay:
#### No coding questions: 
- go to https://www.ebay.com and search for “lg phone”
- what type of search request is eBay using, GET or POST?           
Get
- which URL variable represents the search term?          
The variable "_nkw" represents the search term.
- click on “Auction”. Which URL variable represents auction searches?
The variable "LH_Auction" represents auction searches.
- Can you come up with a shorter URL that produces the same search result page?
https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1
The aboce url produces the same search result page
- Click on the next search result page and observe how the URL changes. What variable in the URL identifies the page number?
The variable "_pgn" identifies the page number.
- What is the feature common (in HTML source code) to each item in the search results page? i.e., what item do we need to select to obtain each item among the search results?
If we want to locate the blocks for each item: Tag "li" with class as "s-item s-itempl-on-bottom s-item--watch-at-corner" is the common feature for each item in the page.
If we want to get the name for each item: Tag "H3" with class as "s-itemtitle"is the common feature for the name of each item.

#### Coding questions:
- (1) Use the URL identified above and write code that loads eBay’s search result page for “lg tv”. Save the result to a file.
- (2) Write a loop that will download the first 10 pages of search results (or the maximum result page number, whichever is less). Save each of these pages
IMPORTANT: Each page request needs to be followed by at least a 10 second pause! remember,
you want your program to mimic your behavior as a human and help you make good
purchasing decisions.
- (3) Write a separate piece of code that loops through the pages you downloaded in (b) and opens and parses them into a Python BeautifulSoup-object. Next find the sponsored items on each search result page and print their URL to the screen

### 3 - Imitating Log in behavior with Cookies
#### Preparation: 
- Use your browser to access Planespotters.net, create an account
- Verify that your login works: start an incognito session, navigating to https://www.planespotters.net/user/login , log in, go to your profile page https://www.planespotters.net/member/profile
#### Coding tasks:
- (1) Access https://www.planespotters.net/user/login using a standard GET request. Read and store the cookies received in the response. In addition, parse the response and read (and store to a string variable) the value of the hidden input field that will (most likely) be required in the login process, in this case, the 'csrf' and 'rid' variable.
- (2) Make a post request using the cookies from (1) as well as all required name-value-pairs (including your username and passwords).
- (3) Get the cookies from the response of the post request and add them to your cookies from (1).
- (4) Verifies that you are logged in by accessing the profile page https://www.planespotters.net/member/profile with the saved cookies
- (5) Then, print out the following at the end: (a) The entire BeautifulSoup document of your profile page; (b) All (combined) cookies from (3); A boolean value to show your username is contained in the document in part (5)(a).

### 4 - Review & Practice - Scrap the 'Barnes and Nobel' Top 100 book's information
#### No coding questions:
Use your browsers development tools. Open the network tab and analyze the network for the following:
- go to https://www.barnesandnoble.com and navigate to “Books” > “B&N Top 100”. Have a look at the URL
- navigate to page 2 of “B&N Top 100”. Did the URL change? What type of request is B&N using, GET or POST?
The url changed, a new variable 'page' is introduced. When changing page, B&N is using 'GET' request.
- which URL variable represents the page number? Is there a variable that represents the number of items per page?
'page' is the variable represents the page number. 'Nrpp' is the variable represents the number of items per page. 
- try to modify these numbers to view the first page with 40 items of “B&N Top 100”
The modified url: 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=40&page=1'
-  inspecting the HTML source code of (e), how can we access each book in the list of B&N’s top 40? How can we access each book’s product page URL (e.g., https://www.barnesandnoble.com/w/thelastthing-he-told-me-laura-dave/1137937512?ean=9781501171345)?
Each book is nested in a "div" with class 'row topX-row'
We can access each book's product page by find the 'href' right after each "h3" tag with class = 'product-info-title'. A note here is that we need to add the link of the main page 'https://www.barnesandnoble.com' as prefix to the 'href' we get.

#### Coding questions:
- Use the URL identified above and write code that loads the first page with 40 items per page of “B&N Top 100”.
- Take your code in (a) and create a list of each book’s product page URL. This list should be of length 40
- Write a loop that downloads each product page of the top 40 books in “B&N Top 100”. I.e., save each of these pages to your computer using a meaningful filename
IMPORTANT:
Each page request needs to be followed by at least a 5 second pause! Remember, you want your program to mimic your behavior as a human and help you make good purchasing decisions
- Write a separate piece of code that loops through the pages you downloaded in (c), opens and parses them into a Python or Java xxxxsoup-object. Next, access the “Overview” section of the page and print the first 100 characters of the overview text to screen.

### 5 - Intruduction to Selenium - Automate your Browser
#### Preparation:
- Download the web-driver that works for your browser. Search 'Python Selenium web-driver + the version of your browser' for instructions
- Get Selenium to work on your system.  I.e., try to code something up in Python that starts a browser of your choice, 
#### Coding questions:
- Using Selenium web-driver, open a browser and navigates to google.com, and searches for "askew"
- navigates to google.com, and searches "google in 1998"
- Does these two pages look interesting to you?

### 6 - Advancing Selenium - Scraping Bustbuy Deal of the Day
- Write a script that goes to bestbuy.com, clicks on Deal of the Day
- reads how much time is left for the Deal of the Day and prints the remaining time to screen (console)
IMPORTANT: Please ensure that there are proper delays after each website interaction.
- Clicks on the Deal of the Day (the actual product), clicks on its reviews
- Saves the resulting HTML to your local hard drive as "bestbuy_deal_of_the_day.htm"
- You can then do NLP with these comments!
  
