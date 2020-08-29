import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
import requests
import time


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

#print latest title
def scrape1(url):   
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')
    titles=soup.find_all('div', class_="content_title")
    latest_title = titles[1]
    latest_title = latest_title.a.text
    print(latest_title)

scrape1(url)

#scrape latest news paragraph text
def scrape2(url):
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')
    paragraph=soup.find('div', class_='article_teaser_body')
    latest_paragraph=paragraph.text
    print(latest_paragraph)

scrape2(url)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

def scrape3(url):
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results=soup.prettify()
    images= soup.find_all('div', class_="img")
    source_url = images[0].img["src"]
    featured_image_url =(f"https://www.jpl.nasa.gov{source_url}")
    print(featured_image_url)

scrape3(url)



url="https://space-facts.com/mars/"
tables = pd.read_html(url)
#tables




tables = pd.read_html(str(url))[0]
tables




url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)




html = browser.html
soup = bs(html, 'html.parser')




#print(soup.prettify())




images=soup.find_all('a', class_="itemLink product-item")
print(images)




image_title=soup.find_all('h3')
image_title




#print each title as text
image_title[1].text




#first url
url=images[6]['href']
click_url=f"https://astrogeology.usgs.gov/{url}"
click_url




browser.visit(click_url)
html=browser.html
soup=bs(html,'html.parser')




source_url=soup.find('li')
picture_url=source_url.a['href']
picture_url




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




#print(title_list)




#print(url_list)




print(dictionary)





