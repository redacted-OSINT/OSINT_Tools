print('''
  _____     _____  ____  _____  ___  ____  ____  ____  
 |_   _|   |_   _||_   \|_   _||_  ||_  _||_  _||_  _| 
   | |       | |    |   \ | |    | |_/ /    \ \  / /   
   | |   _   | |    | |\ \| |    |  __'.     \ \/ /    
  _| |__/ | _| |_  _| |_\   |_  _| |  \ \_   _|  |_    
 |________||_____||_____|\____||____||____| |______|   
                                                       
                                                       ''')

import requests
from bs4 import BeautifulSoup

def grab_links(url):
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    tags = soup.find_all('a')
    with open('results.txt', 'a') as f:
        for tag in tags:
            link = tag.get('href')
            f.write(link + '\n')

def main():
    url = input('Enter target URL here: ')
    grab_links(url)

if __name__ == "__main__":
    main()
