#! python3
#Obtém a previsão do tempo de acordo com a localidade.

import json, requests, sys

#Processa a localidade a partir dos argumentos da linha de comando.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])

#Faz download dos dados JSON a partir da API de OpenWeatherMap.org
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' %(location)
response = requests.get(url)
response.raise_for_status()

#Carrega dados JSON em uma variável Python.
weatherData = json.loads(response.text)

#Exibe as descrições da previsão do tempo.
w = weatherData['list']
print('Current weather in %s: ' %(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])