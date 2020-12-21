import requests 
from bs4 import BeautifulSoup
import time
import pandas as pd
import io
from json import loads

url = "https://www.merriam-webster.com/dictionary/buoyancy"
url2 = "https://www.merriam-webster.com/dictionary/emotions"

def print_pause(string):
    print(string)
    time.sleep(2)

def read_response_to_df(response):
    dictionary = response.text
    return




def parse_function(url):
    '''Function which prompts a url input, 
    makes a get request from the input and parses the text response
    '''
    #url = input("Input the URL you would like to scrape: ")
    # The Res variable stores the HTTP response. E.g Response 200 or 404 error. 
    response = requests.get(url)
    print_pause(f"Response recieved: {response}")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find_all('h1'))
    synonym = soup.find_all('a', attrs={"class": "mw_t_sc"})
    print(synonym)
    #print(soup.body.contents)
    return

if __name__ == '__main__':
    parse_function(url2)