import mysql.connector
from mysql.connector import Error



# Connect to MySQL database
try:
    print('Connecting to MySQL database...')
    conn = mysql.connector.connect(host='localhost',
                                   database='cadastro',
                                   user='root',
                                   password='arg47910113AM')
    if conn.is_connected():
        print('connection established.')
        cursor = conn.cursor()

except Error as e:
    print(e)

def insere(ins_nome, ins_sexo):
	# Data insert
	cursor.execute("insert into pessoas(nome,sexo) values(%s,%s)",(ins_nome, ins_sexo))
	conn.commit()

# Pede os dados ao usuário
name = input("NOME: ")
sex = input("SEXO: ")
insere(name,sex)

# Exibe todos os registros
cursor.execute("select * from pessoas where id = %s" %cursor.lastrowid)
for row in cursor:
	print(row)

conn.close()
print('Connection closed.')
