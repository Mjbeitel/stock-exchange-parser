
import requests

from bs4 import BeautifulSoup

page = requests.get("https://money.cnn.com/data/hotstocks/index.html") # request to download google html page

i = 0

number = []
price = []
change = []
percent = []
company = []

# change = [] could do in excel

error = 'Page is unable to be reached\n'
success = 'Page successfully reached\n'

if page.status_code != 200:
    print(error)

else:

    print(success)

soup = BeautifulSoup(page.content, 'html.parser') # parse url

date  = soup.find('div', class_ = 'wsod_StockTimestamp')

stock_cont = soup.find_all('td', class_ = 'wsod_aRight') # find all

x = range(len(stock_cont)) # capture length



price = soup.find_all('td', class_ = 'wsod_aRight')


print(date.get_text())


print("\n Stock Price:     Change:      %Change:      Company name:")
print(" ---------------------------------------------------------")
for link in soup.find_all('td', class_ = 'wsod_aRight'):

    i = i + 1



    number = link.get_text() # load all values into array. 


    if i % 3 == 1: # divide  by 3 if remainder is 1 

        price = number
        company = link.span.attrs['streamfeed']

       # print(price) # works
        
    if i % 3 == 2:  # divide  by 3 if remainder is 2 

        change = number
       # print(change) # works

    if i % 3 == 0:

        percentage = number 

        print( "    ",price, "     ", change,"     ",percentage,"     ", company)
       

                       
   

