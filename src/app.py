import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def convertidor_de_millones(x):
    #Esta funcion me va a ayudar a poner todos los billones y millones correspondiente a su valor real
    if x.endswith("B"):
        new_value = float(x.replace("B",""))
        return new_value * 1000
    elif x.endswith("M"):
        new_value = float(x.replace("M",""))
        return new_value



#---CONECTAR API---
url = "https://ycharts.com/companies/TSLA/revenues"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
response = requests.get(url, headers = headers)

#Ahora tenemos todo el HTML
html_data = response.text

#Ahora usaremos BeautifulSoup para poder buscar en el HMTL
soup = BeautifulSoup(html_data, "html.parser")

#Ahora buscaremos las tablas que tenemos en nuestro HTML
tables = soup.find_all('table')



#---DATA FRAME---
tesla_revenue = pd.DataFrame(columns= ["Date", "Revenue"])

#Agregar valores al DataFrame
for i in range(2):
    for row in tables[i].tbody.find_all("tr"):
        col = row.find_all("td")
        Date = col[0].text
        Revenue = col[1].text.strip()
        tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({
            "Date":Date,
            "Revenue":Revenue
        }, index=[0])], ignore_index=True)

#Aplicar convertidor de Billones y Millones a nuestro data frame
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].apply(convertidor_de_millones)
#Convertir Data en una fecha mas maneable
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])


#Visualizacion de la nueva tabla
view_table_1 = tesla_revenue.sort_values(by="Date")

plt.figure(figsize=(15, 10))
plt.plot(view_table_1['Date'], view_table_1['Revenue'], marker='o', linestyle='-', color='r')

plt.title('Revenue de Tesla por Trimestre')
plt.xlabel('Date')
plt.ylabel('Revenue (en millones)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("view_1.png")

#---VISUALIZAR DATOS #2---

