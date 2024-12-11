import mysql.connector, requests, xmltodict
from mysql.connector import Error


"""
*************************************************************
*   http://servicos.cptec.inpe.br/XML/                      *
* Primeira cidade com código 220 e última com 5903          *
* Pára em 5726 (Zé Doca) e continua em 5741 (Altônia)       *
* até 5810 (planaltina)                                     *
* continua do 5821 (Ilha Grande) até 5834 (Vida Nova)       *
* continua do 5841 (Campo de Santana) até 5903 (Nazária)    *
************************************************************* 
220 - 5726
5741 - 5810
5821 - 5834
5841 - 5903
"""

"""
range - Python
220, 5727
5741, 5811
5821, 5835
5841, 5904

5507+70+14+63 = 5654 (total de cidades)
"""


# Connect to MySQL database
try:
    print('Connecting to MySQL database...')
    conn = mysql.connector.connect(host='localhost',
                                   database='meteorologia',
                                   user='root',
                                   password='arg47910113AM')
    if conn.is_connected():
        print('connection established.')
        cursor = conn.cursor()

except Error as e:
    print(e)


for cod_cidade in range(5841, 5904):
  resp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/%s/previsao.xml' %cod_cidade)
  dct_temp = xmltodict.parse(resp.text)
  print('{0} - {1} - {2}'.format(cod_cidade, dct_temp['cidade']['nome'], dct_temp['cidade']['uf']))
  cursor.execute("insert into cidades(id_cidade,cidade,estado) values(%s,%s,%s)",
                (cod_cidade, dct_temp['cidade']['nome'], dct_temp['cidade']['uf']))


conn.commit()
conn.close()
print('Connection closed.')
