import matplotlib.pyplot as plt


# Valores de x e y
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Plota uma linha gradiente azul, sem contorno, e expessura s=40
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

# Salva o gráfico em um arquivo
# bbox_inches='tight' remove espaços extras em branco podendo ser omitido
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()
