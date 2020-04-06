#!/home/joaofortunato/.virtualenvs/pmp_price_tracker/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import random

# Reads input data file and returns corresponding variable
def get_input_data(file_name, var_name):
    f = open(file_name, "r")
    for line in f:
        words = line.split(sep="=")
        if words[0].strip() == var_name:
            return words[1].strip()
    return -1

# Scrapes website and returns current price of the course
def price_scraper(url):
    # Defines a user agent and sends a get request
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    headers = {'User-Agent': user_agent}
    page = requests.get(url,headers=headers)

    # Finds span attribute which contains the current price
    soup = bs(page.content, 'html.parser')
    price_text = soup.find("span", class_="price-text__current").text

    # Manipulates the current price string and converts to float
    price = float(price_text.split("€")[-1].strip())

    return price

print(price_scraper(get_input_data("input_data","URL")))
