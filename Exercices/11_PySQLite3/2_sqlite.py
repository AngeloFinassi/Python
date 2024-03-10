import sqlite3
try:
    banco = sqlite3.connect("fd.db")
    cursor = banco.cursor()

    #cursor.execute("INSERT INTO people VALUES('João',20,'joão_loco@gmail.com')")
    cursor.execute("DELETE from people WHERE years = 40")
    banco.commit()
    banco.close()
    print("Dados Excluidos com sucesso")

except sqlite3.Error as erro:
    #em cima, salva o metodo erro em uma variavel tipo subistituit
    print("Erro ao Excluir", erro)