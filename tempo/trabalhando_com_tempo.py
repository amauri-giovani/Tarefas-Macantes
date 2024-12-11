#! python3
#Trabalhando com o tempo, data e hora.

#**************************************************************************************************************************************************
# O Unix epoch(Era Unix ou Época Unix) é uma referência de tempo comumente usada em programação: 00:00hora de 1 de janeiro de 1970 UTC(Universal
# Time Coordinate, ou Tempo Universal Coordenado). A função time.time() retorna o número de segundos desde esse momento na forma de um valor de
# ponto flutuante(que é somente um número com ponto decimal). Esse número é chamado de epoch imestamp.
#**************************************************************************************************************************************************

import time, datetime

time.sleep(1)							#o programa fica travado durante 1 segundo. Se colocar 1000 será = 1000 segundos. Não adianta usar CTRL+C.

print(time.time())						#exibe os segundos desde a Unix epoch.
print(round(time.time(), 2))			#exibe um valor arredondado e com 2 casas decimais.

print(datetime.datetime.now())						#exibe a hora atual no formato padrão americano. 2016-05-01 03:34:07.888265.
print(datetime.datetime.fromtimestamp(1000))		#exibe 1000 segundos após o Unix epoch.
print(datetime.datetime.fromtimestamp(0))			#exibe a data do Unix epoch de acordo com o fuso horário local: 1969-12-31 22:00:00.
print(datetime.datetime.fromtimestamp(time.time()))	#faz o mesmo que datetime.datetime.now(). Exibe a hora atual no formato padrão americano.
dt = datetime.datetime(2016,5,1,3,49,0)				#armazena a data e hora especificada na variável "dt".
print(dt.year, dt.month, dt.second)					#exibe separadamente ano, mês e segundos.
print(dt.hour, dt.minute, dt.second)				#exibe separadamente hora, minuto e segundos.
print(dt == datetime.datetime.now())				#compara a data de "dt" com a atual e retorna True ou False.
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)		#armazena uma duração de tempo em "delta"
print(delta.days, delta.seconds, delta.microseconds)					#exibe dias, segundos e microsegundos de delta.
print(delta.total_seconds())											#retorna a duração somente em segundos.
thousandDays = datetime.timedelta(days=1000)							#armazena em "thousandDays" uma duração de 1000 dias.
print(dt + thousandDays)												#soma "dt" com 1000 dias.
print(delta + thousandDays)												#soma "dt" com 1000 dias.
oct21st = datetime.datetime(2015,10,21,16,29,0)							#armazena uma data em "oct21st".
trintaAnos = datetime.timedelta(days=365*30)							#armazena uma duração de 30 anos em "trintaAnos".
print(oct21st - trintaAnos)												#subtrai 30 anos da data de "oct21st".
print(oct21st.strftime('%d/%m/%Y'))										#exibe a data formatada. ****Ver tabela abaixo.****
print(oct21st.strftime('%d/%m/%Y %H:%M:%S'))							#exibe a data formatada. ****Ver tabela abaixo.****
print(datetime.datetime.now().strftime('%H:%M:%S'))						#exibe hora atual formatada.
data = '27/04/2015 10:03:55'											#armazena uma data no formato EXATAMENTE IGUAL ao formato datetime.
print('strptime: ',datetime.datetime.strptime(data,'%d/%m/%Y %H:%M:%S'))				#converte a string "data" em formato EXATAMENTE IGUAL ao datetime.


#****************************************************************************************************************************************************
#	As datas e horas em Python podem envolver vários tipos diferentes de dados e de funções. A seguir, apresentamos uma revisão dos 3 tipos 
#	diferentes de valores usados para representar tempo:
#
#	- Um timestamp Unix epoch(usado pelo módulo time) é um valor de ponto flutuante ou inteiro correspondente ao número de segundos desde a zero 
#	hora do dia 1 de janeiro de 1970, UTC.
#	- Um objeto datetime(do módulo datetime) contém inteiros armazenados nos atributos, year, month, day, hour, minute e second.
#	- Um objeto timedelta(do módulo datetime) representa uma duração e não um instante específico.
#
#
#	A seguir, uma revisão das funções de tempo, seus parâmetros e os valores de retorno.
#
#	- A função time.time() retorna um valor de ponto flutuante correspondente ao timestamp epoch do instante atual.
#	- A função time.sleep(seconds) interrompe o programa pela quantidade de segundos especificada através do argumento seconds.
#	- A função datetime.datetime(year, month, day, hour, minute, second) retorna um objeto datetime para o instante especificado pelos argumentos.
#	Se os argumentos hour, minute e second não forem especificados, 0 será usado como default.
#	- A função datetime.datetime.now() retorna um objeto datetime para o instante atual.
#	- A função datetime.datetime.fromtimestamp(epoch) retorna um objeto datetime do instante representado pelo argumento de timestamp epoch.
#	- A função datetime.timedelta(weeks, days, hours, minutes, seconds, miliseconds, microseconds) retorna um objeto timedelta que representa uma 
#	duração. Os argumentos nomeados da função são todos opcionais e não incluem month ou year.
#	- O método total_seconds() para objetos timedelta retorna o número de segundos representado pelo objeto timedelta.
#	- O método strftime(format) retorna uma string com o tempo representado pelo objeto datetime em um formato personalizado, baseado na string 
#	format. Consulte a tabela de Diretivas de strftime/strptime para ver os detalhes de formatação.
#	- A função datetime.datetime.strptime(time_string, format) retorna um objeto datetime do instante especificado por time_string, cujo parse 
#	será feito com o argumento de string format. Consulte a tabela de Diretivas de strftime/strptime para ver os detalhes de formatação.
#
#
#
#	#############################################################################################################################################
#	#					#																														#
#	#	DIRETIVA DE 	#																														#
#	#	strftime e 		#												SIGNIFICADO																#
#	#	strptime		#																														#
#	#					#																														#
#	#*******************************************************************************************************************************************#
#	#		%Y			#		Ano com o século, como em '2016'																				#
#	#*******************************************************************************************************************************************#
#	#		%y			#		Ano sem o século, de '00' a '99' (de 1970 a 2069)																#
#	#*******************************************************************************************************************************************#
#	#		%m			#		Mês com um número decimal, de '01' a '12'																		#
#	#*******************************************************************************************************************************************#
#	#		%B			#		Nome completo do mês, como em 'November'																		#
#	#*******************************************************************************************************************************************#
#	#		%b			#		Nome abreviado do mês, como em 'Nov'																			#
#	#*******************************************************************************************************************************************#
#	#		%d			#		Dia do mês, de '01' a '31'																						#
#	#*******************************************************************************************************************************************#
#	#		%j			#		Dia do ano, de '001' a '366'																					#
#	#*******************************************************************************************************************************************#
#	#		%w			#		Dia da semana, de '0'(domingo) a '6'(sábado)																	#
#	#*******************************************************************************************************************************************#
#	#		%A			#		Nome completo do dia da semana, como em 'Monday'																#
#	#*******************************************************************************************************************************************#
#	#		%a			#		Nome do dia da semana abreviado, como em 'Mon'																	#
#	#*******************************************************************************************************************************************#
#	#		%H			#		Hora(relógio com 24 horas), de '00' a '23'																		#
#	#*******************************************************************************************************************************************#
#	#		%I			#		Hora(relógio com 12 horas), de '01' a '12'																		#
#	#*******************************************************************************************************************************************#
#	#		%M			#		Minuto, de '00' a '59'																							#
#	#*******************************************************************************************************************************************#
#	#		%S			#		Segundo, de '00' a '59'																							#
#	#*******************************************************************************************************************************************#
#	#		%p			#		'AM' ou 'PM'																									#
#	#*******************************************************************************************************************************************#
#	#		%%			#		Caractere literal '%'																							#
#	#############################################################################################################################################
