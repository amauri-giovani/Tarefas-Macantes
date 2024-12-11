#! python3
#Inicia um mapa no navegador usando um endereço da linha de comando ou do clipboard.

import webbrowser, sys#, pyperclip										#importa o módulo webbrowser para abrir o navegador.
																		#importa o módulo sys para ler a partir da linha de comando.
																		#importa o módulo pyperclip para ler a partir da área de transferência.
if len(sys.argv) > 1:													#como sys.args armazena como 1º elemento o nome do programa, se tiver
																		#mais algo escrito após, será considerado como endereço para Google Maps.
	address = ' '.join(sys.argv[1:])									#Obtém o endereço da linha de comando.
else:																	#se não existir nada após a chamada ao programa.
	address = pyperclip.paste()											#Obtém o endereço do clipboard.

webbrowser.open('https://www.google.com/maps/place/' + address)			#abre o navegador com o endereço solicitado, seja linha de comando ou
																		#área de transferência.
																		
