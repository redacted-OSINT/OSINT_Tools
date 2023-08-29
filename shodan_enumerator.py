print('''
  ______   ____  ____   ___   ______        _      ____  _____                                              
.' ____ \ |_   ||   _|.'   `.|_   _ `.     / \    |_   \|_   _|                                             
| (___ \_|  | |__| | /  .-.  \ | | `. \   / _ \     |   \ | |                                               
 _.____`.   |  __  | | |   | | | |  | |  / ___ \    | |\ \| |                                               
| \____) | _| |  | |_\  `-'  /_| |_.' /_/ /   \ \_ _| |_\   |_                                              
 \______.'|____||____|`.___.'|______.'|____| |____|_____|\____|                                             
 ________ ____  _____ _____  _____ ____    ____ ________ _______         _    _________   ___   _______     
|_   __  |_   \|_   _|_   _||_   _|_   \  /   _|_   __  |_   __ \       / \  |  _   _  |.'   `.|_   __ \    
  | |_ \_| |   \ | |   | |    | |   |   \/   |   | |_ \_| | |__) |     / _ \ |_/ | | \_/  .-.  \ | |__) |   
  |  _| _  | |\ \| |   | '    ' |   | |\  /| |   |  _| _  |  __ /     / ___ \    | |   | |   | | |  __ /    
 _| |__/ |_| |_\   |_   \ \__/ /   _| |_\/_| |_ _| |__/ |_| |  \ \_ _/ /   \ \_ _| |_  \  `-'  /_| |  \ \_  
|________|_____|\____|   `.__.'   |_____||_____|________|____| |___|____| |____|_____|  `.___.'|____| |___| 
                                                                                                                                                                              
''')

import shodan

query = input('Enter IP or domain name (not including http or https): ')
SHODAN_API_KEY = input('Enter your SHODAN API KEY: ')
api = shodan.Shodan(SHODAN_API_KEY)

def shodan_requests(query, page=1):
    instances = api.search(query, page=1)
    print('Results found: {}'.format(instances['total']))
    for result in instances['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')

shodan_requests(query, page=1)
