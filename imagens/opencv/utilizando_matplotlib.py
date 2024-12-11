# -*- coding: utf-8 -*-

import cv2															#importa o módulo para carregar a imagem.
from matplotlib import pyplot as plt 								#importa o módulo para manipular a imagem.

img = cv2.imread('messi5.jpg',0)									#carrega a imagem
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')			#carrega a imagem em escala cinza "gray".
plt.xticks([]), plt.yticks([])  									#para ocultar valores assinalados nos eixos X e Y
plt.show()															#exibe a imagem com opções de visualização.