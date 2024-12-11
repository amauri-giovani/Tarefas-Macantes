import requests, json							#importa o módulo requests para download da página.
													#importa o módulo sys para ler a linha de comando.
													#importa o módulo json para ler o resultado
print('Buscando...')								#exibe uma mensagem enquanto faz download da página do Google.

res = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&\
key=AIzaSyDYqS1ip-x52ERWpDhCbENLi7xMgCatm94')									#chama a API do Google com a chave de servidor e armazena em "res".
print(res.raise_for_status())													#melhor forma de verificar se houve erro no download.
maps_data = json.loads(res.text)												#lê os dados json e armazena em "maps_data".
print('\n\nMAPS DATA = ', maps_data['results'][0]['geometry']['location'])		#seleciona os campos desejados e exibe na tela.
print('\n', maps_data)
print('\n', res.text)
#Abaixo são exibições na tela somente para conhecimento.
'''
print(maps_data.keys())															#exibe as chaves do resultado.
print(res)																		#retorna em número. Exemplo: se retornar "200" é porque não houve erro.
print(res.text)																	#exibe todo o conteúdo baixado.
print('\n\nTipo: ', type(res))													#exibe o tipo da variável "res".
print(res.json())																#exibe o tipo da variável "res" em formato JSON..
print(res.headers['content-type'])												#exibe o valor de "content-type" na página HTML.
'''