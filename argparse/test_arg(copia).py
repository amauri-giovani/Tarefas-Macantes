import argparse

if __name__ == '__main__':
	# choices = {'client': client, 'server': server}
	parser = argparse.ArgumentParser(description='Opções de instalação do Django')
	# parser.add_argument('role', choices=choices, help='wich role to play')
	parser.add_argument('-i, --ignore', metavar='', type=str, default='',
							help='Ignora a apresentação das informações no final da instalação.')
	args = parser.parse_args()
	# function = choices[args.role]
	# function(args.p)