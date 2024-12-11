# -*- coding: utf-8 -*-


import cv2																	#importa o módulo para manipular a imagem.

#Carrega duas imagens
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.png')

#Colocar o logotipo no canto superior esquerdo, criando um ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

#Agora, criar uma máscara de logotipo e criar sua máscara inversa também
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#Agora, black-out na área de logotipo em ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#Tome única região do logotipo da imagem do logotipo.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

#Colocar logotipo em ROI e modificar a imagem principal.
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('res1',mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('res2',img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('res3',img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('res4',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('res4',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

