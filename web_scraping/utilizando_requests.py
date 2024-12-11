# -*- coding: utf-8 -*-
#! python3
#Utilizando o módulo requests para realizar downloads da internet através de uma URL.

import requests, os																#importa o módulo requests.

# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')		#armazena em "res" o conteúdo da página.
# print(type(res))																#verifica o tipo de objeto, no caso, requests.
# print(res.status_code == requests.codes.ok)										#verifica se não ocorreu erro no download.
# print(res.status_code)															#retorna 200 se não ocorreu erro no download.
# print(res.raise_for_status())													#melhor forma de verificar se houve erro no download.
# print(len(res.text))															#verifica o tamanho do download.
# #print(res.text[:250])															#exibe o texto do download.
# playFile = open('RomeueJulieta.txt', 'wb')										#cria um arquivo do tipo binário em modo leitura.
# for chunk in res.iter_content(100000):											#percorre o arquivo em porções de 100.000 bytes.
# 	playFile.write(chunk)														#escreve no arquivo as porções de iter_content.
# playFile.close()																#fecha o arquivo.


# O método iter_content() retorna porções do conteúdo a cada iteração pelo loop. Cada porção tem o tipo de dado bytes e é possível especificar 
# quantos bytes terá. Cem mil bytes geralmente é um bom tamanho, portanto passe 100000 como argumento para iter_content()
# O uso do loop for e de iter_content() podem parecer complicados se comparados ao fluxo de trabalho com open()/write()/close() que usamos
# para gravar arquivos-texto, porém servem para garantir que o módulo requests não consuma muita memória mesmo que asrquivos enormes sejam 
# baixados. Você poderá conhecer outros recursos do módulo requests em http://requests.readthedocs.org .


# Download de arquivos
url = "http://www.saudedica.com.br/wp-content/uploads/2014/03/morangos.jpg"
r = requests.get(url)
with open(os.path.basename(url), "wb") as code:
    code.write(r.content)