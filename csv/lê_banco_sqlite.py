import sqlite3

connection = sqlite3.connect('first.sqlite')

cursor = connection.cursor()

# Ambos modos abaixo mostram todos os dados do banco de dados


 # MODO 1
sql = cursor.execute("SELECT * FROM lua")
#sql = cursor.execute("SELECT * FROM lua WHERE nome = 'Amauri' ")

for row in sql:
    print (row)
#    print (row[1:3])
'''
RESPOSTA: Linha por linha
(1, 'ana', '11/11/11')
(2, 'Amauri', '31/10/1974')
(3, 'Fernanda', '25/04/2002')
(4, 'Ana Paula', '23/12/1973')
(5, 'Roger', '25/12/2012')
(6, 'Romeu', '12/10/1978')
(7, 'helena', '23/5/1994')
(8, 'Rafael', '11/11/1992')
(9, 'Carla', '30/09/1977')
(10, 'Alfredo', '15/04/1976')
(11, 'aa', 12)
(12, 'we', 22)

'''
'''
# MODO 2
cursor.execute("SELECT * FROM lua")# WHERE nome = 'Amauri'")
var = cursor.fetchall()
print(var)

RESPOSTA: Tudo na mesma linha
[(1, 'ana', '11/11/11'), (2, 'Amauri', '31/10/1974'), (3, 'Fernanda', '25/04/2002'), (4, 'Ana Paula', '23/12/1973'), (5, 'Roger', '25/12/2012'), (6, 'Romeu', '12/10/1978'), (7, 'helena', '23/5/1994'), (8, 'Rafael', '11/11/1992'), (9, 'Carla', '30/09/1977'), (10, 'Alfredo', '15/04/1976'), (11, 'aa', 12), (12, 'we', 22)]
'''


connection.commit()

connection.close()
