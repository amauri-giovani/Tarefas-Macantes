import matplotlib.pyplot as plt


# Valores de x e y
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Plota pontos com expessura s=200
plt.scatter(x_values, y_values, s=100)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
