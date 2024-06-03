from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/catalogue/page-{}.html'
bookpricelist = []
with open('bookpricelist.txt', 'w') as file:
    for i in range(1, 26):  # The site has 50 pages
        urlpage = url.format(i)
        response = requests.get(urlpage)
        if response.status_code == 200:  # Check if the page was fetched successfully
            page = response.content
            soup = BeautifulSoup(page, 'html.parser')
            articles = soup.find_all('article', class_='product_pod')
            for article in articles:
                bookname = article.h3.a['title']
                bookprice = article.find('p', class_='price_color').text.strip()
                bookpricelist.append(bookname + '-' + bookprice)
                file.write(bookname + '-' + bookprice + '\n')
        else:
            print(f"Failed to retrieve page {i}")

print(bookpricelist[:10])
