#my api full stack project 





import mysql.connector as sql
import sqlite3
import requests
import pandas as pd 
import numpy as np 
import plotly.express as px 



#replace the "demo" apikey below with your own key 
url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AMZN,MSFT,NVDA&RANGE=2024-05-01&RANGE=2024-05-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=DF1S1NJLNRR7506D'

r = requests.get(url)
data = r.json()

keys = []
organized_information = {}

# if calling options history, use lines below to input date and ticker 
input_date = input(f'Input a date: [XXXX-XX-XX]')
input_ticker = input(f'Input 1 ticker:')
input_table = input (f'Name the table:[ticker:date(XXXX-XX-XX)]')
url2 = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={input_ticker}&apikey=DF1S1NJLNRR7506D&date={input_date}'
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
display_info = pd.DataFrame(access_data)
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

    


#Connecting to MySQL database
conn = sql.connect(
    user='root',
    password='ok',
    host='localhost',
    database='testdb'
)
# change tables column according to the data in your api pull 
try:
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS company_name (
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

    conn.commit()

    #sql insert statements for each dictionary in access_data
    for option in access_data:
        columns = ', '.join(option.keys())
        placeholders = ', '.join(['%s'] * len(option))
        sql_insert = f"INSERT INTO options ({columns}) VALUES ({placeholders})"
        values = list(option.values())
        cursor.execute(sql_insert, values)

    conn.commit()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

print("Data inserted")


print (access_data)

