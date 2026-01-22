import numpy as np
import time
from matplotlib import pyplot as plt

def func2(n):
    def pro_matrizes(a,b):
        return a@b
    tempos2= []
    tempos3= []
    tempos4= [] 
    
    potencias = [2,3,4]

    m = np.rand(n,n)

    
    for potencia in potencias:
        result = m
        to = time.time()
        for i in range(potencia-1):
            result = pro_matrizes(result,m)
        t = time.time()
        if(potencia == 2):
            tempos2.append(t-to)
        elif(potencia == 3):
            tempos3.append(t-to)
        else:
            tempos4.append(t-to)

    return tempos2 , tempos3, tempos4


    

n2 = [500,1000,1500]
tempos_dimensao = []
for i in range(len(n2)):
    tempos_dimensao.append(func2(n2[i]))

print(tempos_dimensao)


# código do matplotlib

