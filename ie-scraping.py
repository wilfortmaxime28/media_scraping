import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs



scheme = 'https'
target_host= 'lenouvelliste.com'
target_url= f'{scheme}://www.{target_host}'
print (target_url)

free_proxy_url='https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt'  # TODO



# get the proxy as http response
# TODO

# Convert the http response to list of proxy
# TODO

#def get_random_proxy(array):
#	''' get a random proxy '''
#	proxy = random.choice(array)

	# to get more info on the proxy format
	# More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
#	return # {'protocol': 'ip:port'} # TODO

def get_random_proxy (proxy_list):
    proxy = random.choice(proxy_list)
    return{
        'http':proxy,
    }

def get_working_proxy ():
    res = requests.get(free_proxy_url)
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


# set a custom header
headers = {
	'Host': target_host,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9, image/avif,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br', # TODO
}

# call and get the proxy
proxy = get_working_proxy()
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