#! python 3
#Abre vários resultados de pesquisa no Google.

import requests, sys, webbrowser, bs4				#importa o módulo requests para download da página.
													#importa o módulo sys para ler a linha de comando.
													#importa o módulo webbrowser para abrir o navegador.
													#importa o módulo bs4 para busca mais precisa com BeautifulSoup.

print('Buscando...')								#exibe uma mensagem enquanto faz download da página do Google.

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))		#faz a pesquisa de acordo com a linha de comando, sem o nome do programa [0]
res.raise_for_status()															#verifica se ocorreu algum erro.

soup = bs4.BeautifulSoup(res.text, "html.parser")						#Obtém os links dos principais resultados da pesquisa.

linkElems = soup.select('.r a')											#seleciona os elementos <a> que estiverem na class="r". Através da inspeção de
																		#elementos é possível verificar que antes de <a> existe uma class="r".
numOpen = min(5, len(linkElems))										#verifica com a função min() qual valor é menor, ou seja, se encontrou 5 ou se 
																		#o total foi menor que 5. Então armazena em "numOpen" a menor quantidade de 
																		#buscas encontradas. A função max() faz o contrário, verifica qual é maior.
for i in range(numOpen):												#faz um loop de acordo com o número armazenado em "numOpen", 5 ou menos.
	webbrowser.open('http://google.com' + linkElems[i].get('href'))		#abre uma aba do navegador para cada resultado.



#print(linkElems[0].getText())											#exibe somente o texto do elemento 0 sem as tags.

#print(linkElems)
#print(res.text)
#print(len(linkElems))