from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
# import pandas_ta
import warnings
warnings.filterwarnings('ignore')

sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

# symbols cleanup - some symbols contain dots ".", we need to replace them with "-" so we can read data with yfinance
sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-')

# grab list with all the stock symbols
symbols_list = sp500['Symbol'].unique().tolist()

print(symbols_list)