import mysql.connector
from connect_db import Conndb


# Connect to MySQL database
conexao = Conndb()
try:
  conexao.cursor.execute("select cidade from cidades where id < 20")

  for cid in conexao.cursor:
    print(str(cid[0]))

  # for cod_cidade in range(5841, 5904):
  #   resp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/%s/previsao.xml' %cod_cidade)
  #   dct_temp = xmltodict.parse(resp.text)
  #   print('{0} - {1} - {2}'.format(cod_cidade, dct_temp['cidade']['nome'], dct_temp['cidade']['uf']))
  #   cursor.execute("insert into cidades(id_cidade,cidade,estado) values(%s,%s,%s)",
  #                 (cod_cidade, dct_temp['cidade']['nome'], dct_temp['cidade']['uf']))

finally:
  conexao.cursor.close()
  conexao.conn.close()
print('Connection closed.')
