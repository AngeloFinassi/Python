import sqlite3
#Cria banco de dados
banco = sqlite3.connect("fd.db")

#cursor possiblita mexer no banco com comandos SQL
cursor = banco.cursor()

#cria uma tabela
""" cursor.execute("CREATE TABLE people (nome text, years integer, email text)") """

#cursor.execute("INSERT INTO people VALUES('João',20,'joão_loco@gmail.com')")

#garante que que foi adicionado algo
#banco.commit()

#Para enchergar a tabela
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())