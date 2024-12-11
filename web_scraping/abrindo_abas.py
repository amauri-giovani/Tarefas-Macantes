#! python3
#Inicia um mapa no navegador com as páginas descritas em url*

import webbrowser


b = webbrowser.get('google-chrome')
b.open_new('https://web.whatsapp.com/')
b.open('https://web.skype.com/en/')
b.open('https://web.telegram.org/#/im')