import requests 
from bs4 import BeautifulSoup
import time
import pandas as pd
import io
from json import loads

def print_pause(string):
    print(string)
    time.sleep(2)

def read_response_to_df(response):
    dictionary = response.text
    return

def parse_function():
    '''Function which prompts a url input, 
    makes a get request from the input and parses the text response
    '''
    url = input("Input the URL you would like to scrape: ")
    # The Res variable stores the HTTP response. E.g Response 200 or 404 error. 
    response = requests.get(url)
    print(response.json())
    print(response)
    print_pause(f"Response recieved: {response}")
    read_response_to_df(response)
    content = requests.get(url).content
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup.body.contents)
    return

if __name__ == '__main__':
    parse_function()