import numpy as np
from matplotlib import pyplot as plt

n = 100

cord_x = np.random.rand(n)
cord_y = np.random.rand(n)
cord_x_pontos = []
cord_y_pontos = []

def esta_na_regiao(x,y):
    if(y <= 1-x):
        return True
    return False

for i in range(n):
    if(esta_na_regiao(cord_x[i], cord_y[i])):
        cord_x_pontos.append(float(cord_x[i]))
        cord_y_pontos.append(float(cord_y[i]))


def func(x):
    return 1-x

dom = np.linspace(0.0, 1.0, 100)
imagem = func(dom)


plt.plot(cord_x_pontos, cord_y_pontos, marker = 'o', linestyle = '')
plt.plot(dom,imagem,)
plt.show()

