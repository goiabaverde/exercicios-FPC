import numpy as np
import time
from matplotlib import pyplot as plt


def func1(n):

    a = np.ones(n)
    b = np.ones(n)

    alpha = np.random.rand()
    beta = np.random.rand()

    for i in range(n):
        x = np.random.rand()
        a[i] = x
        y = np.random.rand()
        b[i] = y

    c = alpha * a + beta * b
    

    return c
n1 = [10**4, 10**5, 10**6, 10**7]
tempos = []

for i in range(len(n1)):
    t0 = time.time()
    func1(n1[i])
    t = time.time()
    tempos.append(t-t0)

plt.figure()
plt.plot(n1,tempos, marker ='o', linestyle = '')
plt.title("Tempo de execução em função da dimenssão (Escala linear)")
plt.xlabel("Dimensão")
plt.ylabel("Tempod execução (s)")
plt.legend()
plt.grid(True)
plt.show()