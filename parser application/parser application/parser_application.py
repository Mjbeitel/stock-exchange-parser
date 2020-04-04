
import requests
import xlsxwriter 
import pandas as pd
import os

from bs4 import BeautifulSoup

page = requests.get("https://money.cnn.com/data/hotstocks/index.html") # request to download google html page

################################################## INITALIZATIONS ######################################################


date = []
number = []
prices = []
changes = []
percentages = []
companies = []
i = 0

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

workbook = xlsxwriter.Workbook('stock-exchange-data.xlsx')
workbook.close() # close excel if left open

############################################################# URL PARSE FUNCTION ###############################################################

def stock_parse(i):
    for link in soup.find_all('td', class_ = 'wsod_aRight'):

        i = i + 1



        number = link.get_text() # load all values into array. 


        if i % 3 == 1: # divide  by 3 if remainder is 1 

            price = number # print out current price

            prices.append(price) # append price

            company = link.span.attrs['streamfeed']

            companies.append(company)
        
        if i % 3 == 2:  # divide  by 3 if remainder is 2 

            change = number

            changes.append(change)
           # print(change) # works

        if i % 3 == 0:

            percentage = number

            percentages.append(percentage)

            print( "    ",price, "     ", change,"     ",percentage,"     ", company)


############################################################### EXCEL PRINTING FUNCTION #######################################################

def print_excel(changes,percentages,prices,companies,date,i):
    workbook = xlsxwriter.Workbook('stock-exchange-data.xlsx') 
  

    worksheet = workbook.add_worksheet(date.get_text()) # adds new worksheet
  

    worksheet.add_table('A2:D32', {'style':'Table Style Dark 2' , 'columns': [{'header': 'Company'},
                                           {'header': 'Price'},
                                           {'header': 'Change'},
                                           {'header': '%Change'},
                                           ]}) # add  data able 

    merge_format = workbook.add_format({ # format of merge
        'bold': 1,
        'font_size': 18,
        'align': 'left',
        'valign': 'vcenter'})

    worksheet.merge_range('A1:D1', 'Stock Exchange Data', merge_format)

    worksheet.set_column('A:A', 30) # set column A width
    worksheet.set_column('B:D', 12) # set column B-D width

    worksheet.write('A2', 'Company') # write data to cells 
    worksheet.write('B2', 'Price') 
    worksheet.write('C2', 'Change') 
    worksheet.write('D2', '%Change') 

    #worksheet.write_row('A3',companies[1]) does not work well



    worksheet.write('A33',date.get_text()) # print date of collection


    row = 2
    col = 0

    # Iterate over the data and write it out row by row. 
    for item in companies : 
   
        # write operation perform 
        worksheet.write(row, col, item) 
  
        # incrementing the value of row by one 
        # with each iteratons. 
        row += 1


    row = 2
    col = col + 1 # incriment column

    for item in prices : #prices array
   
        # write operation perform 
        worksheet.write(row, col, item) 
  
        # incrementing the value of row by one 
        # with each iteratons. 
        row += 1

    row = 2
    col = col + 1 # incriment column


    for item in changes : # changes array
   
        # write operation perform 
        worksheet.write(row, col, item) 
  
        # incrementing the value of row by one 
        # with each iteratons. 
        row += 1

    row = 2
    col = col + 1 # incriment column


    for item in percentages : # show percentages
  
        # write operation perform 
        worksheet.write(row, col, item) 
  
        # incrementing the value of row by one 
        # with each iteratons. 
        row += 1



    workbook.close() # close excel file with all new information

def excel_opener():

     os.system('stock-exchange-data.xlsx') # open excel file 


############################################# MAIN ###################################################

stock_parse(i) # call parser

print_excel(changes,percentages,prices,companies,date,i) # call excel printer

excel_opener() # open excel file

    
