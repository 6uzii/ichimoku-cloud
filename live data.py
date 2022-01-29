#!/usr/bin/env python
# coding: utf-8

# In[6]:


# used to get data
import yfinance as yf   
 
# gets the data for the stock Apple by specifying the stock ticker, start date, and end date 
data = yf.download('AAPL','2016-01-01','2018-01-01') 
 
# Plot the close prices 
import matplotlib.pyplot as plt 
data.Close.plot() 
plt.show() 


# In[1]:


# used to get data
import yfinance as yf

# gets the data for the stock Apple by specifying the stock ticker, period, and interval
intraday_data = yf.download(tickers="AAPL",
                            period="5d",
                            interval="1m",
                            auto_adjust=True)
intraday_data.head()


# In[ ]:




