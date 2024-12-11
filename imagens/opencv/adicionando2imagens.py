# -*- coding: utf-8 -*-

import cv2											#importa o módulo para manipular a imagem.

img1 = cv2.imread('ml.png')							#carrega a 1ª imagem.
img2 = cv2.imread('logo.jpg')						#carrega a 2ª imagem.

print img1.shape									#exibe número de linhas, colunas e canais (se a imagem é de cor).
print img2.shape									#exibe número de linhas, colunas e canais (se a imagem é de cor).

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)			#soma as duas imagens.

cv2.imshow('dst',dst)								#exibe a imagem.
cv2.waitKey(0)										#aguarda o pressionamento de uma tecla.
cv2.destroyAllWindows()								#fecha a janela da imagem.
