#! python3
#Manipulando Imagens com Pillow

from PIL import ImageColor, Image 									#importa o módulo ImageColor para informações de cores.
																	#importa o módulo Image para manipular as imagens.

#Exibe informações em RGBA conforme o nome da cor. O Pillow aceita nomes como "chocolate".
print(ImageColor.getcolor('red', 'RGBA'))							#exibe em modo RGBA as cores. No caso: (255, 0, 0, 255)
print(ImageColor.getcolor('chocolate', 'RGBA'))						#exibe em modo RGBA as cores. No caso: (210, 105, 30, 255)

#Acessa informaçoes sobre a imagem.
catIm = Image.open('pedaco.png')									#abre o arquivo de imagem.
print(catIm.size)													#exibe o tamanho do arquivo de imagem em largura e altura.
width, height = catIm.size 											#atribui o tamanho da imagem à largura e altura.
print(width)														#exibe a largura da imagem.
print(height)														#exibe a altura da imagem.
print(catIm.filename)												#exibe o nome do arquivo de imagem.
print(catIm.format)													#exibe o formato do arquivo de imagem.
print(catIm.format_description)										#exibe o formato do arquivo de imagem com o significado por extenso.
catIm.save('zophie.jpg')											#salva a imagem com outro formato, no caso, JPG.

# #Cria uma nova imagem.
im = Image.new('RGBA', (100,200), 'purple')							#cria uma nova imagem de tamanho 100x200 na cor rosa.
im.save('purpleImage.png')											#salva a imagem no formato PNG.

#Copiando e colando imagens.
croppedIm = catIm.crop((335,345,565,560))							#recorta um trecho da imagem conforme os pixels SEM AFETAR o original.
croppedIm.save('crooped.png')										#salva a imagem no formato PNG.
catCopyIm = catIm.copy()											#copia a imagem, porém não copia para a área de transferência (clipboard).
faceIm = catIm.crop((335,345,565,560))								#recorta um trecho da imagem conforme os pixels SEM AFETAR o original.
print(faceIm.size)													#exibe o tamanho do arquivo de imagem em largura e altura.
catCopyIm.paste(faceIm, (0,0))										#cola a imagem de catCopyIm sobre a imagem de faceIm na posição (0,0).
catCopyIm.paste(faceIm, (400,500))									#cola a imagem de catCopyIm sobre a imagem de faceIm na posição (400,500).
catCopyIm.save('pasted.png')										#salva a imagem no formato PNG.

#Copiando uma vez e colando várias vezes a mesma imagem no mesmo arquivo.
catImWidth, catImHeight = catIm.size								#atribui o tamanho da imagem à largura e altura.
faceImWidth, faceImHeight = faceIm.size								#atribui o tamanho da imagem à largura e altura.
catCopyTwo = catIm.copy()											#copia a imagem de catIm para catCopyTwo.
for left in range(0, catImWidth, faceImWidth):						#faz um loop de 0 a largura de catIm, em passos da largura de faceIm.
	for top in range(0, catImHeight, faceImHeight):					#faz um loop de 0 a altura de catIm, em passos da altura de faceIm.
		print('LEFT = %d e TOP = %d' %(left, top))					#exibe o valor de "left" e "top".
		catCopyTwo.paste(faceIm, (left, top))						#cola a imagem para a posição correspondente a posição do loop.

catCopyTwo.save('tiled.png')										#Salva a imagem em um novo arquivo.

		
#Redimensionando imagens.





#Rotacionando imagens.




#Imagem espelhada.





lotoIm = Image.open('relatorio_nove.png')									#abre o arquivo de imagem.
lotoImWidth, lotoImHeight = lotoIm.size										#atribui o tamanho da imagem à largura e altura.


# sair = 0
file = open('pixels.txt', 'w')

#Verifica o valor do primeiro pixel que não seja "branco" e exibe saindo do loop.
# for x in range(0, catImWidth):
# 	for y in range(0, catImHeight):
# 		a = catIm.getpixel((x, y))
# 		if a != (255,255,255,255):
# 			print(x,y)
# 			sair = 1
# 			break
# 	if sair == 1:
# 		break

			# im.putpixel((x,y), a)

			# print(x,y,catIm.getpixel((x, y)))
		# file.write(str(x) + ' ' + str(y) + ' ' + str(catIm.getpixel((x,y))) + '\n')


# file.close()

im = Image.new('RGBA', (lotoImWidth,lotoImHeight))							#cria uma nova imagem de tamanho 100x200 na cor rosa.
c = 220

for x in range(0, lotoImWidth):												#para um range iniciado em "0" até a largura do arquivo copiado.
	for y in range(0, lotoImHeight):										#para um range iniciado em "0" até a altura do arquivo copiado.
		a = lotoIm.getpixel((x, y))											#atribui o valor do pixel à variável "a".
		if a >= (c,c,c,c) or a >= (c,c,c):									#compara se "a" é maior ou igual a "c".
			continue														#se for verdadeiro não copia o pixel.
		else:
			im.putpixel((x,y), (0,0,0,255))													#altera o valor do pixel para "preto".		
			file.write(str(x) + ' ' + str(y) + ' ' + str(lotoIm.getpixel((x, y))) + '\n')	#se for falso copia o pixel.

im.save('copyTransparente.png')											#salva a imagem no formato PNG.
file.close()															#fecha o arquivo.