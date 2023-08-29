print('''
           _________  ________  ____  ____  _________              
          |  _   _  ||_   __  ||_  _||_  _||  _   _  |             
          |_/ | | \_|  | |_ \_|  \ \  / /  |_/ | | \_|             
              | |      |  _| _    > `' <       | |                 
             _| |_    _| |__/ | _/ /'`\ \_    _| |_                
  ______   _|_____|  |________||____||____|  |_____|_  ____  ____  
.' ____ \ |_   __  |     / \     |_   __ \   .' ___  ||_   ||   _| 
| (___ \_|  | |_ \_|    / _ \      | |__) | / .'   \_|  | |__| |   
 _.____`.   |  _| _    / ___ \     |  __ /  | |         |  __  |   
| \____) | _| |__/ | _/ /   \ \_  _| |  \ \_\ `.___.'\ _| |  | |_  
 \______.'|________||____| |____||____| |___|`.____ .'|____||____| 
                                                                   
                                                                   ''')

target = input('Enter target website: ')
search_term = input('Enter search term: ')

def search():
    import requests
    text = requests.get(target).text
    #search = text.find(search_term)
    if search_term in text:
        print(f'{search_term} is present.')
    else:
        print(f'{search_term} not present.')

search()

