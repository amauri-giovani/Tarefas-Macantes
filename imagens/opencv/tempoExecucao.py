#! python2
# -*- coding: utf-8 -*-

import cv2                                      	#importa o módulo para manipular a imagem.

e1 = cv2.getTickCount()								#armazena o valor do tempo que iniciou o script.
# your code execution
img = cv2.imread('messi5.jpg', 0)					#carrega a imagem em escala cinza "0".
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)		#tamanho da tela para exibir s imagem.
cv2.imshow('image',img)								#exibe a imagem.
cv2.waitKey(0)										#aguarda o pressionamento de qualquer tecla.
cv2.destroyAllWindows()								#fecha a imagem.
cv2.imwrite('messigray.png',img)					#salva a imagem com outro formato.

e2 = cv2.getTickCount()								#armazena o valor do tempo que terminou o script.
time = (e2 - e1)/ cv2.getTickFrequency()			#subtrai o tempo final do tempo inicial do script.

print 'e1 =', e1									#exibe o valor de "e1".
print 'e2 =', e2									#exibe o valor de "e2".
print 'Frequência =', cv2.getTickFrequency()		#exibe o valor da frequência.
print 'Tempo =', time								##exibe o valor do tempo gasto para execução do script.