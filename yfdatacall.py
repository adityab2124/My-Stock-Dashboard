import requests 
import mysql.connector as sql 
import yfinance as yf 
import pandas as pd

# yf api, downloading quarterly stock data 
msft_data = yf.download('AAPL', start='2018-01-01', end='2024-06-01', interval='3mo')
goog_data = yf.download('AMZN', start='2018-01-01', end='2024-06-01', interval='3mo')
meta_data = yf.download('NVDA', start='2018-01-01', end='2024-06-01', interval='3mo')







#Reseting the index to include the date as a column
msft_data.reset_index(inplace=True)
msft_data.rename(columns={'index': 'Date'}, inplace=True)
goog_data.reset_index(inplace=True)
goog_data.rename(columns={'index': 'Date'}, inplace=True)
meta_data.reset_index(inplace=True)
meta_data.rename(columns={'index': 'Date'}, inplace=True)

msft_data['ticker'] = 'AAPL'
goog_data['ticker'] = 'AMZN'
meta_data['ticker'] = 'NVDA'


conn = sql.connect(
    host='testok.c1022qyui6nf.us-east-2.rds.amazonaws.com',
    user='root',
    password='okpassdat!',
    database='awstest'
)
cursor = conn.cursor()

#sql table insert 
cursor.execute('''
    CREATE TABLE competitorsdata(
        id INT PRIMARY KEY AUTO_INCREMENT,
        ticker VARCHAR(10),
        date DATE,
        open DECIMAL(10, 2),
        high DECIMAL(10, 2),
        low DECIMAL(10, 2),
        close DECIMAL(10, 2),
        adj_close DECIMAL(10, 2),
        volume BIGINT
        
    )
''')


#Convert the DataFrame to a list of dictionaries
data_dicts = msft_data.to_dict(orient='records')
data_dicts_goog = goog_data.to_dict(orient='records')
data_dicts_meta= meta_data.to_dict(orient='records')

#Insert each dictionary into the database
for record in data_dicts:
    columns = ', '.join([col.lower().replace(' ', '_') for col in record.keys()])  # Convert keys to match table column names
    placeholders = ', '.join(['%s'] * len(record))
    sql_insert = f"INSERT INTO competitorsdata ({columns}) VALUES ({placeholders})"
    values = list(record.values())
    cursor.execute(sql_insert, values)
for record in data_dicts_goog:
    columns = ', '.join([col.lower().replace(' ', '_') for col in record.keys()])  # Convert keys to match table column names
    placeholders = ', '.join(['%s'] * len(record))
    sql_insert = f"INSERT INTO competitorsdata ({columns}) VALUES ({placeholders})"
    values = list(record.values())
    cursor.execute(sql_insert, values)

for record in data_dicts_meta:
    columns = ', '.join([col.lower().replace(' ', '_') for col in record.keys()])  #Convert keys to match table column names
    placeholders = ', '.join(['%s'] * len(record))
    sql_insert = f"INSERT INTO competitorsdata ({columns}) VALUES ({placeholders})"
    values = list(record.values())
    cursor.execute(sql_insert, values)









#Close connection and commit changes 
conn.commit()
cursor.close()
conn.close()

print ('Success')
