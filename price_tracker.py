#!/home/joaofortunato/.virtualenvs/pmp_price_tracker/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import smtplib, ssl

# Reads input data file and returns corresponding variable
def get_input_data(file_name, var_name):
    with open(file_name, "r") as f:
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

# Checks if current price is smaller or close to historic minimum price
# Updates data file if needed
def min_price_check(current_price):
    min_price = float(get_input_data("input_data","MIN_PRICE"))

    if min_price == -1 or current_price < min_price:
        # Updates data file to add line for min_price_check
        return True
    elif current_price == min_price:
        return True
    else:
        return False
#Given the receiver, sender emails and a message it sends an email
def send_email_alert(sender_email, recipient_email, password, message):
    port = 465 # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message)
    return

def main():
    data_file = "input_data"

    url = get_input_data(data_file,"URL")
    current_price = price_scraper(url)

    if min_price_check(current_price):
        sender_email = get_input_data(data_file, "SENDER_EMAIL")
        recipient_email = get_input_data(data_file, "RECIPIENT_EMAIL")
        password = get_input_data(data_file, "PASSWORD")

        message = "Subject: PMP Course - Price Altert \n\n Current course price is " +\
        str(current_price) + "."
        send_email_alert(sender_email, recipient_email, password, message)

if __name__ == "__main__":
    main()
