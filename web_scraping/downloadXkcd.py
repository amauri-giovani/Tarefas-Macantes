#! python3
#Faz download de todas as tirinhas de XKCD.

import requests, os, bs4						#importa requests para download da página, os para o sistema e bs4 para retornar um objeto BeautifulSoup.

url = 'http://xkcd.com'										#URL inicial
os.makedirs('xkcd', exist_ok=True)							#armazena as tirinhas em ./xkcd. A chamada "os.makedirs()" garante que essa pasta exista e
															#o argumento "exist_ok=True" impede que a função lance uma exceção caso essa pasta já exista.

print('Abrindo o navegador Firefox ....')

while not url.endswith('#'):								#o loop será encerrado quando a URL terminar em "#".
	#Faz download da página.
	print('Downloading page %s ...' %(url))					#exibe uma mensagem para o usuário saber que o download está sendo feito.
	res = requests.get(url)									#faz o download da página.
	res.raise_for_status()									#verifica se ocorreu algum erro.

	soup = bs4.BeautifulSoup(res.text, "html.parser")		#obtém um objeto BeautifulSoup em "soup".

	#Encontra o URL da imagem da tirinha.
	comicElem = soup.select('#comic img')						#seleciona o seletor CSS onde o elemento "img" se encontra, dentro da div "comic".
	if comicElem == []:											#caso não encontre, exibe a mensagem abaixo.
		print('Não foi possível encontrar imagem cómica.')		#exibe a mensagem informando que não encontrou a imagem.
	else:														#caso encontre a imagem, executa o download conforme comandos abaixo.
		comicUrl = comicElem[0].get('src')						#o atributo "src" poderá ser obtido desse elemento "img" e passado para requests.get()
																#para que o download do arquivo com a imagem da tirinha seja feito.
		#Faz download da imagem.
		print('Baixando imagem em http:%s ...' %(comicUrl))		#exibe a mensagem junto com a URL da imagem que está sendo baixada.
		res = requests.get('http:' + comicUrl)					#faz download da imagem. Nesse caso foi necessário acrescentar o "http:" para a URL.
		res.raise_for_status()									#verifica se ocorreu algum erro.

		#Salva a imagem em ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')	#cria um arquivo em "xkcd" de acordo com seu nome que é o último do path.
		for chunk in res.iter_content(100000):										#percorre o arquivo em porções de 100.000 bytes.
			imageFile.write(chunk)													#escreve no arquivo as porções de iter_content.
		imageFile.close()															#fecha o arquivo.

	#Obtém o URL do botão Prev.
	prevLink = soup.select('a[rel="prev"]')[0]					#o seletor 'a[rel="prev"]' identifica o elemento <a> cujo atributo "rel" está definido como 
																#"prev" e o atributo "href" desse elemento <a> poderá ser usado para obter o URL da tirinha 
																#anterior, que será armazenado em "url".
	url = 'http://xkcd.com' + prevLink.get('href')				#obtém o link da próxima imagem.

print('Download realizado com sucesso!')						#exibe mensagem informando que deu tudo certo.
