import matplotlib.pyplot as plt


# Plota um ponto com expessura s=200
plt.scatter(2, 4, s=200)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
