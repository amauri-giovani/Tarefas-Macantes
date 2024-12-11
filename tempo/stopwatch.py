#! python3
#Simples cronômetro.

import time

#Exibe as instruções do programa.
print('Pressione ENTER para começar. Depois, pressione ENTER para registrar o tempo no cronômetro. Pressione CTRL+C para sair.')
input()
print('Início da contagem de tempo.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Rodada %s: %s (%s) %s %s' %(lapNum, totalTime, lapTime, startTime, lastTime), end='')
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
	#Trata a excessão de CTRL+C para evitar que sua mensagem de erro seja exibida.
	print('\nFIM')