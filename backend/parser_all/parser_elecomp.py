import requests
from bs4 import BeautifulSoup

def format_product_info(title, product_url, stock, price):
    return {
        "title": title,
        "product_url": product_url,
        "stock": stock,
        "price": price
    }

def search_products(query):
    base_url = "https://elecomp.ru"
    search_url = f"{base_url}/search/"

    params = {
        "query": query,
        "sort": "name",
        "order": "asc"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
    }

    try:
        response = requests.get(search_url, params=params, headers=headers)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            product_blocks = soup.find_all("div", class_="product-list__content")
            print(f"Found {len(product_blocks)} product blocks")
            results = []

            if product_blocks:
                for product in product_blocks[:10]:
                    title_tag = product.find("a", class_="product-list__name")
                    title = title_tag.text.strip() if title_tag else "Название не найдено"
                    
                    product_url_tag = title_tag
                    product_url = f"{base_url}{product_url_tag['href']}" if product_url_tag else "URL не найден"

                    stock_tag = product.find("div", class_="product-stock")
                    stock = stock_tag.text.strip() if stock_tag else "Нет данных о наличии"

                    price_tag = product.find_next("span", class_="product-list__price price")
                    price = price_tag.text.strip() if price_tag else "Цена не указана"

                    results.append(format_product_info(title, product_url, stock, price))

                return results if results else None
            else:
                return None
        else:
            return f"Ошибка запроса: {-1}"
    except Exception as e:
        print(f"Произошла ошибка: {-1}")
        return -1

if __name__ == "__main__":
    query = input("Введите наименование или код для поиска: ")
    products = search_products(query)
    if products == -1:
        print("Произошла ошибка при парсинге.")
    elif products:
        for product in products:
            print(product)
    else:
        print("Товары не найдены.")