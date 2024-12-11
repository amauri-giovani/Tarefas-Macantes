# -*- coding: utf-8 -*-
from Tkinter import *
import pygame.mixer
import tkMessageBox
import time
import subprocess
   
sounds = pygame.mixer
sounds.init()

class JanelaCentro(Frame):
	def __init__(self,largura=500, altura=200):
		Frame.__init__(self, )
		self.largura = tela.winfo_screenwidth()
		self.altura = tela.winfo_screenheight()

		x = (self.largura/2) - (largura/2)
		y = (self.altura/2) - (altura/2)

		self.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

def wait_finish(channel):
	while channel.get_busy():
		pass

def button_click():
	if tempo.get() == '':
		tkMessageBox.showwarning("Alerta", "Escolha um tempo.")
	else:
		monitora = time.sleep(int(tempo.get()))
		while monitora > 0:
			monitora -= 1
		lembrete = Tk()
		janela_centro()
		mens = Label(lembrete, text = mensagem.get(), fg = "#000000")
		mens.pack()
		lembrete.mainloop()

		# s = sounds.Sound('alarme.wav')
		# wait_finish(s.play())
		#tkMessageBox.showinfo('Compromisso', mensagem.get())
		#subprocess.Popen(['gedit', '/home/amauri/alarme.txt'])	

		tempo.delete(0, END)

tela = Tk()
principal = JanelaCentro(tela) 
tela.title('Lembrete')
texto = Label(tela, text = 'Você tem um compromisso')
texto.pack()
btOk = Button(tela, text = 'OK', command = button_click)
btOk.pack()
tempo = Entry(font="Arial 18")
tempo.pack()
mensagem = Entry(font="Arial 18")
mensagem.pack()



def shutdown():
    tela.destroy()


tela.protocol("WM_DELETE_WINDOW", shutdown)

tela.mainloop()