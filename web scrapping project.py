import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        
        for quote in quotes:
            print(quote.get_text())
    else:
        print('Failed to fetch the page.')

if __name__ == "__main__":
    scrape_quotes()
