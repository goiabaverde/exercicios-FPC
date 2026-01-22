import numpy as np
from matplotlib import pyplot as plt

#Pegando os pontos através da função loadtxt
coord = np.loadtxt('ex08\pontos.txt')
# Me devolve uma array do numpy com as coordenas dos pontos

# ===== Plotagem =====

plt.figure(figsize=(10,10))

#Plotagem dos pontos

for pos in coord:
    plt.scatter(pos[0], pos[1], marker = 'o', linestyle = '', color = 'r', label = 'Vértices') 

#Plotagem das arestas

for i in range(coord.shape[0] - 1):
    plt.plot([coord[i][0], coord[i+1][0]], [coord[i][1], coord[i+1][1]], color = 'b')

# Fechar o polígono, liga o primeiro ponto ao último
plt.plot([coord[0][0], coord[coord.shape[0] - 1][0]], [coord[0][1], coord[coord.shape[0] - 1][1]], color = 'b', label = 'Arestas')

plt.xlabel("Eixo x", fontsize = 20)
plt.ylabel("Eixo y", fontsize = 20)
plt.title("Polígonos", fontsize = 30)
plt.grid()
plt.legend()
plt.show()


