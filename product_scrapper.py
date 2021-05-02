#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[ ]:


def make_soup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')


# In[ ]:


def scrapSubs(url):
    soup = make_soup(url)
    items = soup.find_all('li',{'class':'s-item'})
    item_details = []
    for item in items:
        try:
            detail_sec = item.find('div',{'class': 's-item__info'})
            item_url = detail_sec.find('a').get('href')
            item_descr = detail_sec.find('h3',{'class':'s-item__title'}).text
            price_descr = ""
            img_url = item.find('img',{'class':'s-item__image-img'}).get('src')
            for des_pair in item.find_all('div',{'class':'s-item__detail'}):
                text = des_pair.find('span').text
                price_descr=price_descr+" "+text
            item_details.append([item_descr, img_url, item_url, price_descr])
        except AttributeError:
            pass
    return item_details


# In[ ]:


def scrapCategory(category, url):
    out = []
    soup = make_soup(url)
    subCatBlock = soup.find('div',{'class':'b-visualnav__grid'})
    subCategories = subCatBlock.find_all('a')
    title = subCatBlock.find_all('div', {'class':'b-visualnav__title'})
    for i in range(len(subCategories)):
        url_sub = subCategories[i].get('href')
        title_sub = title[i].text
        data_sub = scrapSubs(url_sub)
        print(f'\n{title_sub}\n')
        if(len(data_sub)>0):
            df = pd.DataFrame(np.array(data_sub))
            print(data_sub)
            
            df.to_csv(title_sub+'.csv')


# In[ ]:


scrapCategory("Clothes", "https://www.ebay.com/b/Fashion/bn_7000259856")


# In[ ]:


scrapCategory("software", "https://www.ebay.com/b/Electronics/bn_7000259124")

