import mysql.connector

# configurações de acesso ao MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sakila"
)

# Conectar ao banco de dados
mycursor = mydb.cursor()
    
mycursor.execute("""SELECT MONTH(rental_date) AS mes, COUNT(*) AS total_alugueis
            FROM rental
            GROUP BY mes
            ORDER BY mes;""")

# Iterar pelos resultados
for (mes, total_alugueis) in mycursor:
    print(f'Mês: {mes}, Total de Aluguéis: {total_alugueis}')
