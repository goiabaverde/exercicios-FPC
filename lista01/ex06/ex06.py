from matplotlib import pyplot as plt

sequencias = {1 : [], 2 : [], 3.2 : [], 3.5 : [], 4 : []}

# Construindo a sequência
# Pegando os valores para definir a lista

N = 60
lista_a = [1,2,3.2,3.5,4]

for a in lista_a:
    seq = [0.1]
    for n in range(1,N + 1):
        seq.append((a*seq[n-1])*(1-seq[n-1]))
    
    sequencias[a].append(seq)

# Definindo o domínio do gráfico

dom = []

for i in range(N + 1):
    dom.append(i)

print(dom)

# ===== Plotagem ======

plt.figure(figsize=(8,7))
plt.title("Sequências com diferentes valores para a")
plt.xlabel('Iterações')
plt.ylabel('Valor do elemento na n-ésima iteração')

for a in lista_a:
    plt.plot(dom, sequencias[a][0], label = f'a = {a}')

plt.legend()
plt.show()

    
    

    
    
    
    










