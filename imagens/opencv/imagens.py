# -*- coding: utf-8 -*-

import cv2											#importa o módulo para manipular a imagem.

# Load an color image in grayscale
img = cv2.imread('messi5.jpg', 0)					#carrega a imagem em escala cinza "0".
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)		#tamanho da tela para exibir s imagem.
cv2.imshow('image',img)								#exibe a imagem.
cv2.waitKey(0)										#aguarda o pressionamento de qualquer tecla.
cv2.destroyAllWindows()								#fecha a imagem.
cv2.imwrite('messigray.png',img)					#salva a imagem com outro formato.