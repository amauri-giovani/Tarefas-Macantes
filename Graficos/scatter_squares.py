import matplotlib.pyplot as plt


#plt.scatter(2, 4, s=200)	# define um ponto específico x=2, y=4 e s=200 (tamanho do ponto)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)		# "edgecolor" tira o contorno preto 
# 																		# dos pontos e "c" indica a cor da linha.

# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)	# c em formato RGB com valores de 0 a 1.

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)	# cmap para gradiente.

# Define o título do gráfico e nomeia os eixos
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
# plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')	# salva o gráfico e tira os espaços em branco.
plt.show()					# exibe o gráfico.