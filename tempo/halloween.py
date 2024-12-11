#! python3
#Aguarda até que a data do Halloween chegue.

import datetime, time									#importa os módulos.

halloween = datetime.datetime(2016,10,31,0,0,0)			#armazena uma data em "halloween".
while datetime.datetime.now() < halloween:				#fica no loop enquanto não chegar a data do halloween.
	time.sleep(1)										#verifica de 1 em 1 segundo se a data chegou.
	