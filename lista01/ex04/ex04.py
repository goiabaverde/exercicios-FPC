import numpy as np
from matplotlib import pyplot as plt

def pi(n):
    sum = 0
    for i in range(n-1):
        sum += ((-1)**(i+1))/(3+2*(i))
    return 4*(1+sum)

k = 10000

erros = []

valores = []

for i in range(1, k + 1):
    valores.append(i)



for n in valores:
    erros.append(np.pi - pi(n))

print(erros)
    
