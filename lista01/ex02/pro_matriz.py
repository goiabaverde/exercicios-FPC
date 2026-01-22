import numpy as np
import time
from matplotlib import pyplot as plt


def pro_matriz(a,b):
    # Checando se o que recebe como argumento são realmente matrizes 2D do numpy

    if(a.ndim != 2 or b.ndim != 2):
        raise ValueError(f"Os elementos de entrada precisam ser matrizes quadradas")

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



#Inicializas as listas para armazernar os tempos decorridos com cada produto de matrizes

tempos_alg = []
tempos_numpy = []
dimensoes = [50,100,150,200,250]

def pro_matriz_algelin(r):
    # Criar as matrizes de dimensão r
    m1 = np.ones(shape = (r,r))
    m2 = np.ones(shape = (r,r))
    # Coloca em cada elemento dessa matriz valores aleatórios
    for i in range(r):    
        for j in range(r):
            m1[i][j] = np.random.rand()
            m2[i][j] = np.random.rand()
    to = time.time()
    pro_matriz(m1,m2)
    t = time.time()
        
    return t-to

def pro_matriz_numpy(r):
    m1 = np.random.rand(r,r)
    m2 = np.random.rand(r,r)
    to = time.time()
    m1 @ m2
    t = time.time()

    return t - to

for i in range(len(dimensoes)):
    tempos_alg.append(pro_matriz_algelin(dimensoes[i]))
    tempos_numpy.append(pro_matriz_numpy(dimensoes[i]))


print(tempos_alg)
print(tempos_numpy)




    

