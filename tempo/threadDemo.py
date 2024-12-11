#! python3
# Multithreading ou Multitarefas - Utilizando o módulo threading.

import threading, time								#importa o módulo threading para realizar mais tarefas ao mesmo tempo e time para tempo.

print('Start program...')							#exibe a mensagem de início do programa.

def takeANap():										#início da função.
	time.sleep(5)									#aguarda 5 segundos para continuar a executar a função.
	print('Wake up!')								#exibe a mensagem 'Wake up'('acorde').

threadObj = threading.Thread(target=takeANap)		#cria o objeto Thread passando o argumento nomeado target=takeANap e não takeANap().
threadObj.start()									#cria a nova thread e inicia a execução da função alvo na nova thread.

print('End program...')								#exibe a mensagem de fim do programa.


######################
# Saída do programa: #
#					 #
# Start program...   #
# End program... 	 #
# Wake up!			 #
######################

# O motivo pelo qual Wake up! é apresentado depois deve-se ao fato de que, quando threadObj.start() é chamado, a função alvo de threadObj é 
# executada em uma nova thread de execução. A thread principal continua executando em print('End program...'). Enquanto isso, a nova thread
# que estava executando a chamada time.sleep(5) faz uma pausa de 5 segundos. Depois de acordar de seu cochilo de 5 segundos, ela exibirá
# 'Wake up!' e retornará da função takeANap(). Cronologicamente, 'Wake up!' é a última informação exibida pelo programa.
# Um programa Python não terminará até que todas as suas threads tenham terminado. Ao executar esse programa, apesar de a thread original 
# ter terminado, a segunda thread ainda estava executando a chamada a time.sleep(5).



# Passando argumentos à função-alvo da thread.
threadObj2 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})		#modo correto de passar argumentos
																										#para a função print.
																										#kwargs é o que será exibido entre
																										#o que estiver em args

threadObj2.start()																						#inicia a outra thread