import requests
from bs4 import BeautifulSoup
import time
import pandas as pd 

base_url = "https://www.dictionaryofobscuresorrows.com"
urls = []
urls.append(base_url)
all_data = []


def find_content(soup):
    ''' Parse through the input soup - site content
    find all instances of a new post/emotion. 
    Create a dictionary that inputs all the important information 
    for each emotion. i.e the emotion, description and source. 
    Append each entry to a list.
    '''
    try: 
        emotions = soup.find_all('h2')
        post = soup.find_all('div', attrs={"class": "post text"})
        for entry in post:
            source = entry.find('a', href=True)
            link = source['href']
            title = entry.find('h2').text
            content = entry.find('p').text
            entry_dict = {
                "emotion": title,
                "description": content,
                "source":  link
            }
            all_data.append(entry_dict)
        return
    except AttributeError as err:
        print(err)

def get_next_url(soup):
    next_url = soup.find_all('div', attrs={"id": "pageNav"})
    for entry in next_url:
        link = entry.find('a', href=True)
        next_link = link['href']
        if '17' not in next_link: 
            urls.append(str(base_url + next_link))
        elif '17' in next_link:
            print("pass")
        


def parse_site(response):
    ''' Function that takes url input, 
    gets response and returns the site content. 
    '''
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        find_content(soup)
        get_next_url(soup)
        # convert the list of dictionaries to a pandas dataframe
        df = pd.DataFrame(all_data)
        df.to_csv("dictionary_of_sorrows.csv", index=False)
        return 
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def parse_pages():
    ''' main function to parse several urls
    '''
    while len(urls) > 0:
        print(urls)
        url = urls.pop(0)
        response = requests.get(url)
        print(f" Response recieved: {response}")
        parse_site(response)
    return


if __name__ == "__main__":
    parse_pages()