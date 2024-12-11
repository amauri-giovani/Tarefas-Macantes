# coding:utf-8
#!/usr/bin/env python3
# Programação de Redes com Python
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_broadcast.py
# cliente e servidor UDP para o envio de mensagens broadcast em uma LAN local


import argparse, socket


BUFFSIZE = 65535


def server(interface, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((interface, port))
	print('Listening for datagrams at {} - {}'.format(sock.getsockname(), socket.gethostname()))
	while True:
		data, address = sock.recvfrom(BUFFSIZE)
		text = data.decode('utf-8')
		print('The client at {} {!r}'.format(address, text))


def client(network, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	text = '\nNome: ' + socket.gethostname() + '\nMessage: Broadcast datagram!'
	sock.sendto(text.encode('utf-8'), (network, port))


if __name__ == '__main__':
	choices = {'client': client, 'server': server}
	parser = argparse.ArgumentParser(description='Send, receive UDO broadcast')
	parser.add_argument('role', choices=choices, help='wich role to take')
	parser.add_argument('host', help='interface the server listens at;'
						' network the client sends to')
	parser.add_argument('-p', metavar='PORT', type=int, default=1060,
						help='UDP port (default 1060')
	args = parser.parse_args()
	function = choices[args.role]
	function(args.host, args.p)
