#file to just test quick api pulls and dataframes 

#yfinancetest
import pandas as pd 
import yfinance as yf 
import requests

#allow js arguments to pass in 
# data_pass_back = 'Send this to node process'
# input = sys.argv[1]
# output = data_pass_back
# print (output)

# sys.stdout.flush()


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=6URY3WAZ0FIXD5G7'
r = requests.get(url)
data = r.json()
read = pd.read_csv('website_data.csv')

# data.info()
read.info()
read.plot()
# get options history then figure out how to get output to translate into html text 
