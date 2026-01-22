import numpy as np
from matplotlib import pyplot as plt


def y_funcao_x(vo: float, angulo: float, x: float):

    # Converte o angulo inicialmente em graus para radianos

    ang_rad = np.radians(angulo)

    # Calcula a altura em relação a horizontal do corpo dados os parâmetros de velocidade inicial, angulo de lançamento e posição ao longo do eixo x

    y = (x * np.tan(ang_rad)) - ((9.81*(x**2))/(2*((vo*np.cos(ang_rad))**2)))

    return y

# ===== Testes =====

#Alguns parâmetros de angulos velocidades inciais

lista_angulos= [30,45,60, 90, 135]
lista_vo = [5,10,20,15, 10]

# ===== Plotagem =====

plt.figure(figsize=(10,10))
plt.title("Lançamento oblíquo com campo gravitacional constante")
plt.xlabel("Eixo x (m)")
plt.ylabel("Eixo y (m)")

for i in range(len(lista_angulos)):

    ang_rad = np.radians(lista_angulos[i])

    # Encontrando o alcance máximo para ajustar o domínio da função 

    alc_max = ((lista_vo[i]**2) * (np.sin(2*ang_rad)))/(9.81)

    dom = np.linspace(0, alc_max , 1000)
    imagem = y_funcao_x(lista_vo[i], lista_angulos[i], dom)

    plt.plot(dom, imagem, label = f'trajetória para vo = {lista_vo[i]} m/s e ângulo = {lista_angulos[i]}' )

plt.legend()
plt.grid()
plt.show()




