#! python3
#Calcula tempo de execução do programa.

import time 																	#importa o módulo time.

def calcProd():																	#início da função calcProd.
	#Calcula o produto dos 100.000 primeiros números.
	product = 1																	#atribui o valor inteiro 1 à variável "product".
	for i in range(1,1001):														#executa 100000 vezes o loop.
		product *= i 															#calcula o produto vezes o valor de i que vai de 1 a 100.000.
	return product																#retorna o valor da variável "product".

startTime = time.time()															#atribui o valor de time.time() à variável "startTime".
prod = calcProd()																#chama a função calcProd e atribui o retorno à variável "prod".
endTime = time.time()															#atribui o valor de time.time() à variável "endTime".
print(type(endTime))
print('O resultado é %s longos dígitos.' %(len(str(prod))))						#exibe o valor de "prod" no formato string.
print('Levou %s segundos para calcular.' %(endTime - startTime))				#exibe o tempo que o programa levou para executar.