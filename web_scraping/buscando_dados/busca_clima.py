import requests, bs4


resp = requests.get("http://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp")
# print(resp.text)
soup = bs4.BeautifulSoup(resp.text, "html.parser")			#cria um objeto BeautifulSoup e armazena em "exampleSoup".
elems = soup.select('p[arial-label]')	
"""####################################################################
lista = [text for text in soup.stripped_strings]
print(lista)
""" ###################################################################
dia_atual = soup.select('#momento-data')[0].getText()
# print(dia_atual)
dia_semana = dia_atual[:dia_atual.index('\n')]
dia_mes_ano = dia_atual[dia_atual.index('\n')+17:dia_atual.index('T')]
frase_tempo = dia_atual[dia_atual.index('T'):]
print(dia_semana, dia_mes_ano)
print(frase_tempo)
print(soup.select('#momento-localidade')[0].getText(), soup.select('#momento-temperatura')[0].getText())
print("Temperatura Máxima:", elems[0].getText())
print("Temperatura Mínima:", elems[1].getText())
