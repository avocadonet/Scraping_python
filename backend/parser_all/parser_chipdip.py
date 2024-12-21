import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def format_product_info(title, product_url, stock, price):
    return {
        "title": title,
        "product_url": product_url,
        "stock": stock,
        "price": price
    }

def search_products(query):
    base_url = "https://www.chipdip.ru"
    encoded_query = quote(query)
    search_url = f"{base_url}/search/?searchtext={encoded_query}"

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
        response = requests.get(search_url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            product_blocks = soup.find_all("tr", class_="with-hover")
            results = []

            if product_blocks:
                for product in product_blocks[:10]:
                    title_tag = product.find("a", class_="link")
                    title = title_tag.text.strip() if title_tag else "Название не найдено"

                    product_url_tag = title_tag
                    product_url = f"{base_url}{product_url_tag['href']}" if product_url_tag else "URL не найден"

                    stock_tag = product.find("span", class_="nw")
                    if stock_tag:
                        stock_text = stock_tag.get_text(strip=True)
                        stock = stock_text.split()[0]
                    else:
                        stock = "Нет данных о наличии"

                    price_tag = product.find("span", class_="price-main")
                    price = price_tag.text.strip() if price_tag else "Цена не указана"

                    results.append(format_product_info(title, product_url, stock, price))

                return results if results else None
            else:
                return None
        else:
            return f"Ошибка запроса: {-1}"
    except Exception as e:
        print(f"Произошла ошибка: {e}")
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