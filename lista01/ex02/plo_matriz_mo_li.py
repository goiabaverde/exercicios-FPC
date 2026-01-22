import numpy as np
import time
from matplotlib import pyplot as plt

def pro_matriz(a,b):
    # Checando se o que recebe como argumento são realmente matrizes 2D do numpy

    if(a.ndim != 2 or b.ndim != 2):
        raise ValueError(f"Os argumentos precisam ser matrizes quadradas")

    if(a.shape[1] != b.shape[0]):
        raise ValueError(f"Erro, o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz")
    
    # Aloca na memória a matriz de saída
    c = np.ones(shape = (a.shape[0], b.shape[1]))

    # Realiza a o produto entre as matrizes

    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            sum = 0
            for k in range(a.shape[1]):
                sum += a[i][k]*b[k][j]
            c[i][j] = sum
    # O loop com i varre as linhas da matriz a, o loop com j varre as colunas da matriz b e a o loop em k varre os elementos da linha de a da coluna de b
    return c

# --------------
# Experimentos
# --------------

#Inicializas as listas para armazernar os tempos decorridos com cada produto de matrizes

tempos_alg = []
tempos_numpy = []
dimensoes = [50,100,150,200,250]

for n in dimensoes:

    a = np.random.rand(n,n)
    b = np.random.rand(n,n)

    to_alg = time.time()
    c_alg = pro_matriz(a,b)
    t_alg = time.time()

    to_numpy = time.time()
    c_np= a @ b
    t_numpy = time.time()

    tempos_alg.append(t_alg - to_alg)
    tempos_numpy.append(t_numpy - to_numpy)



#--------------
# Plotagem
#--------------

plt.figure(figsize=(8,6))
plt.plot(dimensoes, tempos_alg, marker = 'o', )
plt.xlabel = 'Dimensões'
plt.ylabel = 'Tempo de execução (s)'
plt.legend = ""
plt.title = 'Tempo de execução em função da dimenssão'
plt.grid(True)
plt.show()