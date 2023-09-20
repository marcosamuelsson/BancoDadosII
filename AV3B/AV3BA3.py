import mysql.connector

# configurações de acesso ao MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sakila"
)

# conexão com o banco de dados
mycursor = mydb.cursor()

# comando da atividade h da A2, exercício AV3B
mycursor.execute("""SELECT MONTH(rental_date) AS mes, COUNT(*) AS total_alugueis
                FROM rental
                GROUP BY mes
                ORDER BY mes;""")

# obter os resultados 
myresult = mycursor.fetchall()

# percorrer os resultados
for x in myresult:
  print(x)

