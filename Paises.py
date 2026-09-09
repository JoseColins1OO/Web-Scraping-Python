import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
response.encoding = 'utf-8'


texto = BeautifulSoup(response.text, "html.parser")
paises = texto.find_all("div", class_="country")

datos = []

# 4. Iterar sobre cada tarjeta para "pescar" los datos sueltos
for pais in paises:
    # Extraer el título del atributo 'title' dentro de la etiqueta <a>
    paisName = pais.find("h3", class_="country-name").text.strip()

    # Extraer el precio dentro de la clase .price_color
    paisCapital = pais.find("span", class_="country-capital").text.strip()

    population = int(pais.find("span", class_="country-population").text.strip())

    country_area = float(pais.find("span", class_="country-area").text.strip())

    datos.append({
        "paisName": paisName,
        "paisCapital": paisCapital,
        "population": population,
        "country-area": country_area
    })


    # 3. Convertir a DataFrame
df = pd.DataFrame(datos)
df.to_csv("Paises_catalogo.csv", index=False)
print("Scraping exitoso y archivo catalogo_libros.csv creado.")
