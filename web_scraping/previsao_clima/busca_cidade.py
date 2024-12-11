import mysql.connector, requests, xmltodict, re
from mysql.connector import Error
from connect_db import Conndb
from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

"""
*************************************************************
* 	http://servicos.cptec.inpe.br/XML/						*
*	Primeira cidade com código 220 e última com 5903		*
*	Pára em 5726 (Zé Doca) e continua em 5741 (Altônia)		*
*	até 5834 (Vida Nova) parando em 5810 (planaltina)		*
*	continua do 5821 (Ilha Grande) até 5834 (Vida Nova)		*
*	continua do 5841 (Campo de Santana) até 5903 (Nazária)	*
*************************************************************	
"""

# resp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/%s/previsao.xml' %cod_cidade)
# resp = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades')
# print(resp.text)
# http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml

# Connect to MySQL database
conexao = Conndb()

try:
	conexao.cursor.execute("select cidade from cidades where id < 20")

	for cid in conexao.cursor:
		print(str(cid[0]))

# for cid in cursor:
# 	nome_cid = remover_acentos(str(cid[0]))
# 	print(nome_cid.lower())
# 	resp = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades?city=%s' %nome_cid.lower())
# 	dct_resp = xmltodict.parse(resp.text)
# 	for item in dct_resp:
# 		print(dct_resp['cidades']['cidade']['id'], dct_resp['cidades']['cidade']['nome'], dct_resp['cidades']['cidade']['uf'])

finally:
	conexao.cursor.close()
	conexao.conn.close()
print('Connection closed.')

