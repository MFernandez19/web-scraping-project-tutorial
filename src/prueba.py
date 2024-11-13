
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

#---VISUALIZAR DATOS #1---

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

