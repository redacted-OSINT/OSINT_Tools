print('''
  _____     _____  ____  _____  ___  ____  ____  ____  
 |_   _|   |_   _||_   \|_   _||_  ||_  _||_  _||_  _| 
   | |       | |    |   \ | |    | |_/ /    \ \  / /   
   | |   _   | |    | |\ \| |    |  __'.     \ \/ /    
  _| |__/ | _| |_  _| |_\   |_  _| |  \ \_   _|  |_    
 |________||_____||_____|\____||____||____| |______|   
                                                       
                                                       ''')
print('-' *80)
target = input('Enter target website including http or https: ')
print('-' *80)

import requests
from bs4 import BeautifulSoup

text = requests.get(target).text
soup = BeautifulSoup(text, 'html.parser')
tags = soup.find_all('a')
with open('link.txt', 'w') as f:
    for link in tags:
        results = link.get('href')
        if 'http' in results:
            f.write(results + '\n')
