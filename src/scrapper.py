import requests 
from bs4 import BeautifulSoup
import time

def print_pause(string):
    print(string)
    time.sleep(2)

# The Res variable stores the HTTP response. E.g Response 200 or 404 error. 
res = requests.get("https://www.merriam-webster.com/dictionary/buoyancy")

def parse_function():
   url = input("Input the URL you would like to scrape: ")
   res = requests.get(url)
   print_pause(f"Response recieved: {res}")
   soup = BeautifulSoup(res.text, 'html.parser')
   print(soup.body.contents)
   return

if __name__ == '__main__':
    parse_function()