# coding: utf-8

import sys, platform
from socket import *


serverhost = '10.0.0.17'
serverport = 50006

# message = ["Olá Mundo!"]
message = platform.node()
if len(sys.argv)>1:
	serverhost = sys.argv[1]
	if len(sys.argv)>2:
		message = sys.argv[2:]

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverhost, serverport))

msg = ''

for line in message:
	sockobj.send(line)
	data = sockobj.recv(1024)
	msg += data
	# print ("Client Recebeu: ", repr(data))

print msg
sockobj.close()