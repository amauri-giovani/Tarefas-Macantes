# -*- coding: utf-8 -*-

import cv2                                      #importa o módulo para manipular a imagem.
from matplotlib import pyplot as plt            #importa o módulo para exibir a imagem de forma elegante.

RED = [255,0,0]                                #atribui o valor de cor vermelha "[255,0,0]" à "RED".

img1 = cv2.imread('opencv_logo.png')            #exibe a imagem.


'''
Se você deseja criar uma borda em torno da imagem, algo como uma moldura de foto, você pode usar a função
cv2.copyMakeBorder(). Mas tem mais aplicações para operação de convolução, de zero estofamento etc.
Esta função tem os seguintes argumentos:
src -> imagem de entrada
superior , inferior , esquerda , direita -> largura da borda em número de pixels em direções correspondentes
borderType -> bandeira que define o tipo de borda a ser adicionada. Pode-se os seguintes tipos:
cv2.BORDER_CONSTANT -> Adiciona uma borda colorida constante. O valor deve ser dado como próximo argumento.
cv2.BORDER_REFLECT -> Border será reflexão de espelho dos elementos de fronteira, como este: fedcba | abcdefgh | hgfedcb
cv2.BORDER_REFLECT_101 ou cv2.BORDER_DEFAULT -> Igual ao anterior, mas com uma ligeira alteração, como este: gfedcb | abcdefgh | gfedcba
cv2.BORDER_REPLICATE -> último elemento é replicado por toda parte, como este: aaaaaa | abcdefgh | hhhhhhh
cv2.BORDER_WRAP -> Não posso explicar, ele será parecido com este: cdefgh | abcdefgh | abcdefg
valor -> cor da borda se o tipo de fronteira é cv2.BORDER_CONSTANT
'''

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=RED)


#Exibe as imagens em modo de gráfico. 
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
