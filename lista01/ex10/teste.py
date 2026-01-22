import math
import numpy as np
from matplotlib import pyplot as plt

def trajetória(vo: float, angulo: float, x: float):
    # Converte o angulo inicialmente em graus para radianos

    ang_rad = math.radians(angulo)
    # Calcula a altura em relação a horizontal do corpo dados os parâmetros de velocidade inicial, angulo de lançamento e posição ao longo do eixo x
    y = (x * math.tan(ang_rad)) - ((9.81*(x**2))/(2*((vo*math.cos(ang_rad))**2)))

    return y
dom = np.linspace(0, 100/9.81, 100)
imagem = trajetória(10.0, 45.0, dom)

plt.plot(dom,imagem)
plt.show()

