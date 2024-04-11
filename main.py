from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

url = 'https://listado.mercadolibre.com.pe/iphone-15'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('li', class_='ui-search-layout__item')

print(products)

product_list = []
for product in products:
    title = product.find('h3').get_text()
    price = product.find('span', class_='andes-money-amount__fraction').get_text()
    post_link = product.find("a")["href"]
    img_link = product.find("img")["data-src"]

    product_list.append({
        'title': title,
        'price': price,
        'post_link': post_link,
        'img_link': img_link
    })



app = Flask(__name__, template_folder="layout", static_folder="assets")


@app.route("/")
def home():
    return render_template("./index.html", products=product_list)


if __name__ == "__main__":
    app.run(debug=True)
