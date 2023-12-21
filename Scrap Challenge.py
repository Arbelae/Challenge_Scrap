#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome')


# In[ ]:


# Visit the Mars news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Create a Beautiful Soup object/parcel the HTML
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


# Extract titles and preview text
news_articles = soup.find_all('div', class_='list_text')


# In[ ]:


# Create a list to store dictionaries
news_data = []


# In[ ]:


# Loop through articles and store data in the list
for article in news_articles:
    title = article.find('div', class_='content_title').text
    preview = article.find('div', class_='article_teaser_body').text
    
    # Store data in a dictionary
    article_data = {'title': title, 'preview': preview}
    news_data.append(article_data)
print(news_data)
import json

with open('mars_news_data.json', 'w') as f:
    json.dump(news_data, f)


# In[ ]:


#End the automated browsing session
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




