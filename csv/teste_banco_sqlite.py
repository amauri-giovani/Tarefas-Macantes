import sqlite3

connection = sqlite3.connect('first.sqlite')

cursor = connection.cursor()

#cursor.execute("""SELECT DATE('NOW')""")

'''
cursor.execute("""CREATE TABLE lua (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
nasc DATE NOT NULL)""")
'''
i = True

while(i==True):
    nome_id = input("NOME: ")
    data_nasc = input("DATA NASC.: ")

    cursor.execute("INSERT INTO lua (nome, nasc) VALUES (?,?)", 
                   (nome_id, data_nasc))
    connection.commit()
    continua = input("\nContinuar? (s/n): ")
    if continua == 'n':
        i = False
    


connection.close()

