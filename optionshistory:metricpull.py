#my api project - full stack project 
# Project:
# 1. Scrape data with an API 
# 2. Create a data pipeline from that API into a SQL server
# 3. Host the SQL server on AWS
# 4. Create a Dashboard in Tableau or Power BI that connects to the AWS SQL server
# 5. Publish to a site, so users can visualize/interact with data
import mysql.connector as sql

import requests
import pandas as pd 
import numpy as np 
import plotly.express as px 
import tabulate as tab

url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AMZN,MSFT,NVDA&RANGE=2024-05-01&RANGE=2024-05-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=DF1S1NJLNRR7506D'

r = requests.get(url)
data = r.json()


#date = '2009-06-08'
keys = []
organized_information = {}

#def options_history(): 
input_date = input(f'Input a date: [XXXX-XX-XX]')
input_ticker = input(f'Input 1 ticker:')
insert_table = input('Insert name of table:')
#insert_table = 'Collection'
url2 = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={input_ticker}&apikey=6URY3WAZ0FIXD5G7&date={input_date}'
r2 = requests.get(url2)
data2 = r2.json()
access_data = data2['data'] 
term_list = []
for terms in access_data:
        symbol = terms['symbol']
        expiration = terms['expiration']
        strike = terms['strike']
        type = terms['type']
        last = terms['last']
        mark = terms['mark']
        bid = terms['bid']
        bid_size = terms['bid_size']
        ask = terms['ask']
        ask_size = terms['ask_size']
        volume = terms['volume']
        open_interest = terms['open_interest']
        date = terms['date']
        implied_volatility = terms['implied_volatility']
        delta = terms['delta']
        gamma = terms['gamma']
        rho = terms['rho']
        vega = terms['vega']
        
        
        reorganized_framework ={'Information': {'Type': type, 'Date': date, 'Expiration': expiration,'Strike': strike}, 
                                'Additional Info':{'Mark':mark, 'Last Trade': last, 'Implied Volatility': implied_volatility,
                                                   'Volume': volume, 'Open Interest': open_interest},'Greek':
                                                   {'Delta':delta, 'Gamma':gamma,'Rho':rho,'Vega':vega}}
       # print (reorganized_framework)
    #print (display_info)


        


meta_data = data['meta_data']
payload = data ['payload']
company_name = meta_data ['symbols']
# print (f' These are the tickers for the data requested: \n {symbol_data}')
return_calculations = payload['RETURNS_CALCULATIONS']
means = return_calculations['MEAN']
stddevs = return_calculations['STDDEV']
corr = return_calculations['CORRELATION']
index_elements = corr['index']




dict = {}

for element in index_elements:
    dict2 = {}
    dict[element] = dict2 
    dict2['Mean'] = means[element]
    dict2['Stan.Dev'] = stddevs[element]


conn = sql.connect(
    user='root',
    password='ok',
    host='localhost',
    database='testwork'
)
cursor = conn.cursor()

cursor.execute(f'''
CREATE TABLE {insert_table} (
    id INT PRIMARY KEY AUTO_INCREMENT,
    contractID VARCHAR(255),
    symbol VARCHAR(255),
    expiration DATE,
    strike DECIMAL(10, 2),
    type VARCHAR(50),
    last DECIMAL(10, 2),
    mark DECIMAL(10, 2),
    bid DECIMAL(10, 2),
    bid_size INT,
    ask DECIMAL(10, 2),
    ask_size INT,
    volume INT,
    open_interest INT,
    date DATE,
    implied_volatility DECIMAL(10, 5),
    delta DECIMAL(10, 5),
    gamma DECIMAL(10, 5),
    theta DECIMAL(10, 5),
    vega DECIMAL(10, 5),
    rho DECIMAL(10, 5)
)
''')

for option in access_data:
    columns = ', '.join(option.keys())
    placeholders = ', '.join(['%s'] * len(option))
    oksql = f"INSERT INTO {insert_table} ({columns}) VALUES ({placeholders})"
    values = list(option.values())
    cursor.execute(oksql, values)

conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully")



#####combinedcompanydivs 

