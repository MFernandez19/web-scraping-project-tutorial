

#---SQL---

#Hacer la coneccion y crear el cursos
connection = sqlite3.connect("Tesla.db")
cursor = connection.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS tesla_revenue (Date, Revenue_Million)")

#Ingresar valores a la tabla
for _, row in tesla_revenue.iterrows():
    cursor.execute('''
    INSERT INTO tesla_revenue 
    VALUES (?,?)
    ''',(row["Date"],row["Revenue"]))

connection.commit()

#Ver los datos del SQL
'''
for row in cursor.execute("SELECT * FROM tesla_revenue"):
    print(row)
'''

connection.close()

#---VISUALIZAR DATOS
plt.figure(figsize=(10, 5))
plt.plot(tesla_revenue['Date'], tesla_revenue['Revenue'], marker='o', linestyle='-', color='b')

# Añadir título y etiquetas
plt.title('Revenue de Tesla por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Revenue (en millones)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("Figura_1.png")