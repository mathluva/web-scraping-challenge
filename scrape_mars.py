import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
import requests
import time

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser


def scrape1():  
    browser = init_browser() 
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)
    #scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')
    titles=soup.find_all('div', class_="content_title")

    #print latest title
    latest_title = titles[1]
    latest_title = latest_title.a.text

    #print latest title paragraph
    paragraph=soup.find('div', class_='article_teaser_body')
    latest_paragraph=paragraph.text
    
    #close the browser after scraping
    browser.quit

    return(f"{latest_title}: \n {latest_paragraph}")

#scrape1()

def scrape2():
    browser = init_browser() 
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    images= soup.find_all('div', class_="img")
    source_url = images[0].img["src"]
    featured_image_url =(f"https://www.jpl.nasa.gov{source_url}")

    browser.quit

    return(featured_image_url)

#scrape2()

def scrape3():
    browser = init_browser() 
    url="https://space-facts.com/mars/"
    browser.visit(url)

    time.sleep(1)
    tables = pd.read_html(url)

    #scrape table containing facts about mars
    #convert data to html table string
    tables = pd.read_html(str(url))[0]

    browser.quit
    
    #print(tables)
#scrape3()

def scrape4():
    browser = init_browser() 
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    images=soup.find_all('a', class_="itemLink product-item")

    image_title=soup.find_all('h3')

    url=images[6]['href']

    click_url=f"https://astrogeology.usgs.gov/{url}"

    browser.quit

    browser.visit(click_url)
    html=browser.html
    soup=bs(html,'html.parser')

    source_url=soup.find('li')
    picture_url=source_url.a['href']


    title_list=[]
    url_list=[]
    dictionary=[]
    images = images[: : 2]
    for i in range(len(image_title)):
        title_list.append(image_title[i].text)
        url=images[i]['href']
        click_url=f"https://astrogeology.usgs.gov/{url}"
        browser.visit(click_url)
        time.sleep(1)
        html=browser.html
        soup=bs(html,'html.parser')
        source_url=soup.find('li')
        picture_url=source_url.a['href']
        url_list.append(picture_url)
        dictionary.append({"title":image_title[i].text, "img_url":picture_url})

        browser.quit

    return(url_list)

#scrape4()    

def scrape():
    dic = {}

    dic["scrape1"] = scrape1()
    dic["scrape2"] = scrape2()
    dic["scrape3"] = scrape3()
    dic["scrape4"] = scrape4()

    return(dic)
    
