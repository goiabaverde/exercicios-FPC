import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt



def init(N : int, o : int):
    """
    Função que inicializa o terreno que será uma grade formada por uma matriz quadrada de dimensões N x N e que apresentará o obstáculos em sua estrutura
    """
    if o > N**2 - 1:
        print("Erro, o número de obstáculos inserido deve ser menor ")
        return 1
    
    terreno = np.zeros((N,N)) # Inicializo o terreno
    linhas = np.random.randint(low = 0, high = N, size = o) # Pego as coordenadas das linhas dos obstáculos
    colunas = np.random.randint(low = 0, high = N, size = o) # Pego as coordenadas das colunas dos obstáculos

    # Implentando os obstáculos no terreno

    for i in range(o):
        terreno[linhas[i], colunas[i]] = 2
    while len(np.where(terreno == 2)[0]) < o: # Enquanto não tiver o número estabelecido no argumento da função não cessará a organição dos obstáculos no terreno
        terreno[np.random.randint(low = 0, high = N), np.random.randint(low = 0, high = N)] = 2

    # Verificação que o termo central é necessariamente um elemento alagado

    if terreno[int(N/2), int(N/2)] == 2:
        while len(np.where(terreno == 2)[0]) < o:
            terreno[int(N/2), int(N/2)] = 1
            terreno[np.random.randint(low = 0, high = N ), np.random.randint(low = 0, high = N)] = 2

    terreno[int(N/2), int(N/2)] = 1 # Inicializa o elemento central como alagado
    return terreno



def flood(terreno_inicial):
    """
    Função que dado um terreno_inicial que é uma matriz ele atualizará esse terreno proceguindo com o alagamento
    """
    # Busca as coordenas dos pontos alagados

    coordenadas = np.where(terreno_inicial == 1)

    # Cria uma cópia do terreno inicial o qual foi passado inicialmente e nessa cópia ocorrerão as mudanças de acordo com o alagamento

    terreno_novo = terreno_inicial.copy()

    for i in range(len(coordenadas[0])):
        # Verificação acima
        if coordenadas[0][i] - 1 != -1 and terreno_inicial[coordenadas[0][i] - 1, coordenadas[1][i]] != 2:
            terreno_novo[coordenadas[0][i] - 1, coordenadas[1][i]] = 1
        # Verificação abaixo
        if coordenadas[0][i] != terreno_inicial.shape[0] - 1 and terreno_inicial[coordenadas[0][i] + 1, coordenadas[1][i]] != 2:
            terreno_novo[coordenadas[0][i] + 1, coordenadas[1][i]] = 1
        # Verificação para esquerda
        if coordenadas[1][i] - 1 != -1 and terreno_inicial[coordenadas[0][i], coordenadas[1][i] - 1] != 2:
            terreno_novo[coordenadas[0][i], coordenadas[1][i] - 1] = 1
        # Verificação para direita
        if coordenadas[1][i] != terreno_inicial.shape[0] - 1 and terreno_inicial[coordenadas[0][i], coordenadas[1][i] + 1] != 2:
            terreno_novo[coordenadas[0][i], coordenadas[1][i] + 1] = 1

    return terreno_novo

# Animação do terreno inundando

terreno = init(N = 50, o = 500)

fig, ax = plt.subplots()
ax.set_title("Flooding")
cax = ax.matshow(terreno, cmap = 'Blues')

def update(frame):
    global terreno
    terreno = flood(terreno)
    cax.set_data(terreno)
    return cax
ani = FuncAnimation(fig, update, frames=40, interval = 1)

plt.show()