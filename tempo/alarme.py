#! python3
#abre um aviso no horário programado e toca um som.

import time, subprocess

tempo = int(input("Digite um tempo: "))

while tempo > 0:
	time.sleep(1)
	tempo = tempo -1
	print (tempo)

while True:
	subprocess.Popen(['gedit', '/home/amauri/alarme.txt'])
	subprocess.Popen(['cvlc', '--play-and-exit', '/home/amauri/alarme.mp3'])
	time.sleep(10)



# subprocess.Popen(['see','/home/amauri/alarme.txt'], shell=True)

#vlc://quit                     Item especial para encerrar o VLC


'''
# -*- coding: UTF-8 -*-
import os
import platform # para checagem do sistema operacional
 
host = raw_input("Host:")
execucoes = input("Execucoes:")
 
if platform.system() == "Windows":
    print os.popen("ping -n "+ str(execucoes) + " " + host).read() #sistemas Windows
else:
    print os.popen("ping -c" + str(execucoes) + " " + host).read() #outros sistemas
'''