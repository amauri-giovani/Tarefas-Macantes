# -*- coding: utf-8 -*-

#API Google Maps APIs Web Services Distance Matrix API

import requests, json							#importa o módulo requests para download da página.
													#importa o módulo sys para ler a linha de comando.
													#importa o módulo json para ler o resultado
#print('Buscando...')								#exibe uma mensagem enquanto faz download da página do Google.


a = 'rua antonio do campo'
b = 'rua voluntarios da patria,SP'

res = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&language=pt-BR&\key=AIzaSyDYqS1ip-x52ERWpDhCbENLi7xMgCatm94'%(a,b))									#chama a API do Google com a chave de servidor e armazena em "res".
print(res.raise_for_status())													#melhor forma de verificar se houve erro no download.
maps_data = json.loads(res.text)												#lê os dados json e armazena em "maps_data".
# print('\n\nMAPS DATA = ', maps_data['results'][0]['geometry']['location'])		#seleciona os campos desejados e exibe na tela.
print('\n', maps_data)
print('\n', res.text)

