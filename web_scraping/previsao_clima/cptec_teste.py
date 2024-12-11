import xmltodict, requests, siglas


# resp = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades?city=sao paulo')
# print(resp.status_code)
# print(resp.text)


# dct = xmltodict.parse(resp.text)

# print('\n',dct)

# for item in dct['cidades']['cidade']:
# 	print('{0} - {1}'.format(item['nome'], item['id']))

# print('\n\n')

"""
resp = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades?city=aracaju')#%s' %nome_cid.lower())
dct_resp = xmltodict.parse(resp.text)
for item in dct_resp:
	print(dct_resp['cidades']['cidade']['id'], dct_resp['cidades']['cidade']['nome'], dct_resp['cidades']['cidade']['uf'])
"""


city = input("Cidade (código): ")

# temp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/244/previsao.xml')	# para 4 dias
temp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/7dias/%s/previsao.xml' %city)	# para 7 dias
# print(temp.status_code)
# print(temp.text)

dct_temp = xmltodict.parse(temp.text)

# print(dct_temp['cidade']['nome'], '\n')
print('{0} - {1}'.format(dct_temp['cidade']['nome'], dct_temp['cidade']['uf']))

# for item in dct_temp['cidade']:
	# print(dct_temp['cidade'][item])

# for item in dct_temp['cidade']:	
# print(dct_temp['cidade']['previsao'])

for item in dct_temp['cidade']['previsao']:
	dia = item['dia'].split('-')
	print('{0}/{1}'.format(dia[2], dia[1]))
	tempo = siglas.tempo_clima(item['tempo'])
	print(tempo)
	print('Mín: {0} - Máx: {1}'.format(item['minima'], item['maxima']))

atualizado = dct_temp['cidade']['atualizacao'].split('-')
print('Atualizado em {0}/{1}/{2}'.format(atualizado[2], atualizado[1], atualizado[0]))
	# 
	# print('{0} - {1}'.format(dct_temp['cidade']['maxima'], dct_temp['cidade']['minima']))
	