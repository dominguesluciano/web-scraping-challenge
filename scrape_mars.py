from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
import pymongo
import pandas as pd
from selenium.webdriver.common.by import By

    

def scrape():

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('https://mars.nasa.gov/news/')
    news_title = driver.find_element_by_xpath("//div[@class='content_title']/a")
    news_p = driver.find_element_by_xpath("//div[@class='article_teaser_body']").text

    driver.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    element = driver.find_element_by_css_selector("article")
    attributeValue = element.get_attribute("style")
    featured_image_url = attributeValue.split('\"')[1]

    driver.get('https://twitter.com/marswxreport?lang=en')
    mars_weather = driver.find_element_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")

    driver.get('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    
    hemisphere_image_urls = []

    #loop 4 hemispheres
    for i in range (4):
        img_url = driver.find_element_by_xpath("//div[@class='item']/a[@class='itemLink product-item']").get_attribute("href")
        img_title = driver.find_element_by_xpath("//div[@class='item']/div[@class='description']/a[@class='itemLink product-item']/h3").text
        hemisphere_image_urls.append({"title" : img_title,"image_url": img_url})
    
    output = {
        "news_title": news_title, 
        "news_p": news_p, }
    return output