# -*- coding: utf-8 -*-

from PIL import Image

lotoIm = Image.open('img013.tiff')									#abre o arquivo de imagem.
lotoImWidth, lotoImHeight = lotoIm.size										#atribui o tamanho da imagem à largura e altura.



file = open('pixels.txt', 'w')												#cria o arquivo em modo gravação.

im = Image.new('RGBA', (lotoImWidth,lotoImHeight))							#cria uma nova imagem de tamanho 100x200 na cor rosa.
c = 220																		#atribui o valor "220" à variável "c".

for x in range(0, lotoImWidth):												#para um range iniciado em "0" até a largura do arquivo copiado.
	for y in range(0, lotoImHeight):										#para um range iniciado em "0" até a altura do arquivo copiado.
		a = lotoIm.getpixel((x, y))											#atribui o valor do pixel à variável "a".
		if a >= (c,c,c,c) or a >= (c,c,c):									#compara se "a" é maior ou igual a "c".
			im.putpixel((x,y), (0,0,0,255))													#altera o valor do pixel para "preto".
			file.write(str(x) + ' ' + str(y) + ' ' + str(lotoIm.getpixel((x, y))) + '\n')	#se for falso copia o pixel.
		else:
			im.putpixel((x,y), (255,255,255,255))													#altera o valor do pixel para "preto".
			file.write(str(x) + ' ' + str(y) + ' ' + str(lotoIm.getpixel((x, y))) + '\n')	#se for falso copia o pixel.

im.save('copyPedaco.pdf', 'PDF')												#salva a imagem no formato PNG.
file.close()																#fecha o arquivo.