#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome')


# In[ ]:


# Visit the Mars Temperature Data Site
url = 'https://static.bc-edx.com/data/web/mars_facts/temperature.html'
browser.visit(url)
import pandas as pd


# In[ ]:


# Create a Beautiful Soup object
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


# Extract data from HTML table
table = soup.find('table')
mars_data = pd.read_html(str(table))[0]
# Rename columns as per instructions
mars_data.columns = ['id', 'terrestrial_date', 'sol', 'ls', 'month', 'min_temp', 'pressure']

# Convert data types
mars_data['terrestrial_date'] = pd.to_datetime(mars_data['terrestrial_date'])
mars_data['sol'] = pd.to_numeric(mars_data['sol'])
mars_data['ls'] = pd.to_numeric(mars_data['ls'])
mars_data['month'] = pd.to_numeric(mars_data['month'])
mars_data['min_temp'] = pd.to_numeric(mars_data['min_temp'])
mars_data['pressure'] = pd.to_numeric(mars_data['pressure'])
# How many months exist on Mars?
num_months = mars_data['month'].nunique()

# How many Martian days' worth of data are there?
num_martian_days = mars_data['sol'].nunique()


# In[ ]:


# Visualize average minimum temperature by month
import matplotlib.pyplot as plt

avg_min_temp_by_month = mars_data.groupby('month')['min_temp'].mean()
avg_min_temp_by_month.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Average Min Temperature (Celsius)')
plt.title('Average Minimum Temperature on Mars by Month')
plt.show()
mars_data.to_csv('mars_weather_data.csv', index=False)


# In[ ]:





# In[ ]:




