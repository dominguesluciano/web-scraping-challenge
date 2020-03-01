#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Dependencies
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
import pymongo
import pandas as pd


# In[2]:


driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://mars.nasa.gov/news/');


# In[7]:


#
news_title = driver.find_element_by_xpath("//div[@class='content_title']/a")
news_p = driver.find_element_by_xpath("//div[@class='article_teaser_body']")
print(news_title.text)
print(news_p.text)


# In[8]:


driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars');


# In[9]:


element = driver.find_element_by_css_selector("article")
attributeValue = element.get_attribute("style")
featured_image_url = attributeValue.split('\"')[1]
featured_image_url


# In[10]:


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://twitter.com/marswxreport?lang=en');


# In[18]:


from selenium.webdriver.common.by import By


# In[57]:


mars_weather = driver.find_element_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
print(mars_weather.text)


# In[3]:


driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
url = driver.get('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars');


# In[63]:


#set a dict to receive titles and images urls form 4 mars hemispheres

hemisphere_image_urls = []

#loop 4 hemispheres
for i in range (4):
    img_url = driver.find_element_by_xpath("//div[@class='item']/a[@class='itemLink product-item']").get_attribute("href")
    img_title = driver.find_element_by_xpath("//div[@class='item']/div[@class='description']/a[@class='itemLink product-item']/h3").text
    hemisphere_image_urls.append({"title" : img_title,"image_url": img_url})
    


# In[64]:


hemisphere_image_urls


# In[65]:





# In[ ]:




