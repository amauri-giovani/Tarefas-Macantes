import requests, xmltodict


# 1 = XML, 2 - JSON, 3 - HTML
def busca(data_type, url_change):
	resp = ''
	if data_type == 1:
		resp = requests.get(url_change)
		dct_resp = xmltodict.parse(resp.text)
		resp = dct_resp
	elif data_type == 2:
		resp = requests.get(url_change).json()
	elif data_type == 3:
		resp = requests.get(url_change)
	else:
		print ("ERRO")
	return resp


# print(busca(3,"http://google.com"))
# print(busca(1, 'http://servicos.cptec.inpe.br/XML/cidade/244/previsao.xml'))
print(busca(2, 'https://api.github.com/users/amaurirg'))