from matplotlib.style import available
import requests
from bs4 import BeautifulSoup
import unicodedata

from send_email import send_email

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def get_product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features="lxml")
    
    try:
        title = soup.find(id='productTitle').get_text().strip()
        price_str = soup.find(id='priceblock_ourprice').get_text()
    except:
        return None, None, None
    
    try:
        soup.select('#availability .a-color-success')[0].get_text().strip()
        available = True
    except:
        available = False
    
    try:
        price = unicodedata.normalize("NFKD", price_str)
        price = price.replace(',','.').replace('$','')
        price = float(price)
    except:
        return None, None, None

if __name__ == '__main__':
    url = "https://www.amazon.in/Keychron-Swappable-White-Backlight-Switch/dp/B0836FHCMC/ref=sr_1_3?crid=34VCG5LOCW798&keywords=keyboard+mechanical+mac&qid=1659019456&s=computers&sprefix=%2Ccomputers%2C196&sr=1-3"
    products = [(url, 15000)]
    
    products_below_limit = []
    for product_url, limit in products:
        title, price, available = get_product_info(product_url)
        if title is not None and price < limit and available:
            products_below_limit.append((url, title, price))
        
        if products_below_limit:
            message = "Subject: Price below limit!\n\n"
            message += "Your tracked products are below the given limit!\n\n"
            
            for url, title, price in products_below_limit:
                message += f"{title}\n"
                message += f"Price: {price}\n"
                message += f"{url}\n\n"
            
            send_email(message)