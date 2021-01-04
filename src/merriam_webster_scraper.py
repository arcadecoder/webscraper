import requests 
from bs4 import BeautifulSoup
import time
import pandas as pd
import io
from json import loads
from obscure_scraper import parse_pages

base_url = "https://www.merriam-webster.com/dictionary/emotion"
urls_list = []
parsed_urls = []
urls_list.append(base_url)
final_data = []

def print_pause(string):
    print(string)
    time.sleep(2)

def read_response_to_df(response):
    dictionary = response.text
    return


def get_content():
    return


def get_next_url(soup):
    next_url = soup.find_all('ul', attrs={"class": "mw-list"})
    for entry in next_url:
        synonyms_urls = entry.find_all('a', href=True)
        for entry in synonyms_urls:
            new_url = "https://www.merriam-webster.com" + str(entry['href'])
            if new_url not in parsed_urls:
                urls_list.append(new_url)
                
    return

def parse_site(response):
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        get_next_url(soup)
        urls_list.pop(0)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def parse_pages():
    while len(urls_list) > 0 and len(parsed_urls) < 5:
        url = urls_list[0]
        parsed_urls.append(url)
        response = requests.get(url)
        parse_site(response)
    return

def main():
    parse_pages()
    return


if __name__ == '__main__':
    main()