print('''
     _       _ _                               
    | |     (_) |                              
  __| | __ _ _| |_   _ _ __   _____      _____ 
 / _` |/ _` | | | | | | '_ \ / _ \ \ /\ / / __|
| (_| | (_| | | | |_| | | | |  __/\ V  V /\__ \
 \__,_|\__,_|_|_|\__, |_| |_|\___| \_/\_/ |___/
                  __/ |                        
                 |___/
''')
import requests
from bs4 import BeautifulSoup

def foxnews():
  news = 'https://www.foxnews.com/world/'
  text = requests.get(news).text
  soup = BeautifulSoup(text, 'html.parser')
  tags = soup.find_all(class_="title")

  for tag in tags:
    title = tag.text
    print(f'Result: {title}' + '\n')

def cnn():
  news = 'https://www.cnn.com/world/'
  text = requests.get(news).text
  soup = BeautifulSoup(text, 'html.parser')
  tags = soup.find_all(class_="container__headline-text")

  for tag in tags:
    title = tag.text
    print(f'Result: {title}' + '\n')

def bbc():
    news = 'https://www.bbc.com/news/world'
    text = requests.get(news).text
    soup = BeautifulSoup(text, 'html.parser')
    tags = soup.find_all('a', href=True)

    for tag in tags:
        href = tag['href']
        if 'world-' in href and 'Read morenext' not in tag.text:
            title = tag.text.strip()
            if title:
                print(f'Result: {title}' + '\n')

print('-' *80)
foxnews()
print('-' *80)
cnn()
print('-' *80)
bbc()
print('-' *80)
