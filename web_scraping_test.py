# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:41:47 2022

@author: Mano
"""

import requests
from bs4 import BeautifulSoup as bs
import random

scheme = 'https'
target_host= 'lenouvelliste.com'
target_url= f'{scheme}://www.{target_host}'
print (target_url)
proxy_url='https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt'


headers ={
    'Host': target_host,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9, image/avif,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    }

def get_random_proxy (proxy_list):
    proxy = random.choice(proxy_list)
    return{
        'http':proxy,
        }

def get_working_proxy ():
    res = requests.get(proxy_url)
    proxy_list= res.text.strip().split('\n')
    
    total_tries =20
    print("Getting working proxy...")
    for _ in range (total_tries):
        proxy= get_random_proxy(proxy_list)
        print ('%s) Trying proxy %s' % (_ +1, proxy))
        try:
            res = requests.get('https://google.com', proxies=proxy, timeout=3)
            if res.status_code==200:
                print("One proxy found %s" % proxy)
                return proxy
        except:
            print ("Not good\n")
    print(f'we have tried {total_tries} times(s), but no working proxy found')

proxy= get_working_proxy()

if proxy:  
    try:
        print('Quering %s...'%target_url)
        response = requests.get(target_url, headers=headers, proxies=proxy)
        response.encoding=response.apparent_encoding
        if response.status_code==200:
            print ('Status code :200')
            
            soup = bs (response.text, 'html.parser')
            print('Working')
        else: 
            print('Resquest failed with status code', response.status_code)
    except Exception as err:
        print('Request failed', err)
        
        
