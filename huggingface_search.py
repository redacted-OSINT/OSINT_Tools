print('''
   __                  _           ___            
  / /  __ _____ ____ _(_)__  ___ _/ _/__ ________ 
 / _ \/ // / _ `/ _ `/ / _ \/ _ `/ _/ _ `/ __/ -_)
/_//_/\_,_/\_, /\_, /_/_//_/\_, /_/ \_,_/\__/\__/ 
          /___//___/       /___/
      ''')

#Import Python Libraries
import requests
from bs4 import BeautifulSoup

#Define Search Term
search_term = input('Enter search term here: (If multiple words, separate with + sign) ')

#Define The Hugging Face Search Function
def huggingface_search(search_term):
    base_url = 'https://huggingface.co/'
    models_url = f'{base_url}models?sort=trending&search={search_term}'
    datasets_url = f'{base_url}datasets?sort=trending&search={search_term}'

    models_response = requests.get(models_url).text
    datasets_response = requests.get(datasets_url).text

    models_soup = BeautifulSoup(models_response , 'html.parser')
    datasets_soup = BeautifulSoup(datasets_response , 'html.parser')

    models_results = models_soup.find_all(class_="text-md truncate font-mono text-black dark:group-hover/repo:text-yellow-500 group-hover/repo:text-indigo-600 text-smd")
    datasets_results = datasets_soup.find_all(class_="text-md truncate font-mono text-black dark:group-hover/repo:text-yellow-500 group-hover/repo:text-red-600 text-smd")

    print("Models: (Top 30 Trending)")
    for model in models_results:
        model_name = model.text.strip()
        print("Model Name:", model_name)

    print("\nDatasets: (Top 30 Trending)")
    for dataset in datasets_results:
        dataset_name = dataset.text.strip()
        print("Dataset Name:", dataset_name)

#Execute The Hugging Face Search Function
huggingface_search(search_term)
