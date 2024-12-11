# -*- coding: utf-8 -*-

import cv2 								#importa o módulo para manipular a imagem.

# Load an color image 
img = cv2.imread('messi1bola.jpg')		#carrega a imagem em modo colorido.
px = img[100,100]						#acessa o pixel na posição [100,100].
print px 								#exibe o valor do pixel.
 
# accessing only blue pixel
blue = img[100,100,0]					#atribui o valor do pixel à "blue".
print blue								#exibe o valor do pixel.
img[100,100] = [255,255,255]			#altera o valor do pixel para "branco".
print img[100,100]						#exibe o novo valor do pixel.

# accessing RED value
print img.item(10,10,2)					#acessa o pixel na posição [10,10,2].

# modifying RED value
img.itemset((10,10,2),100)				#modifica o valor do pixel vermelho.
print img.item(10,10,2)					#exibe o novo valor do pixel.
print img.shape							#exibe número de linhas, colunas e canais (se a imagem é de cor).
print img.size							#exibe o número total de pixels da imagem.
print img.dtype 						#exibe o tipo de dados.

# ball = img[273:232, 321:275]
# img[85:227, 134:270] = ball

ball = img[280:340, 330:390]			#informa que a bola está nessa posição.
img[273:333, 100:160] = ball			#altera a imagem atribuindo o valor de "ball".
# img[85:227, 134:270] = ball

# cv2.imwrite('messi2.png',img)			#salva a imagem.

b,g,r = cv2.split(img)					#separa RGB.
# img = cv2.merge((b,g,r))				#Mistura RGB.
img[:,:,2] = 0							#tira o vermelho de RGB da imagem.

cv2.imshow('image',img)					#exibe a imagem.
cv2.waitKey(0)							#aguarda o pressionamento de uma tecla.
cv2.destroyAllWindows()					#fecha a imagem.