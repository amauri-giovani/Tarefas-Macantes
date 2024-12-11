
import requests, xmltodict, siglas


resp = requests.get('http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml')

dct_resp = xmltodict.parse(resp.text)

for capital in dct_resp['capitais']['metar']:
	print(siglas.clima_aeroportos(capital['codigo']))
