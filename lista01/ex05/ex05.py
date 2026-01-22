import numpy as np

def media_mao(seq):
    sum = 0
    for x in seq:
        sum += x
    return sum / len(seq)

def var_mao(seq):
    x_barra = media_mao(seq)
    sum = 0
    for x in seq:
        sum += (x - x_barra)**2
    return sum / (len(seq) - 1)

# Construindo a sequência

seq = [0.1]

    # Pegando os valores para definir a lista

N = 5000
lista_a = [1,2,3.2,3.5,4]

def media_np(seq):
    return np.mean(seq)

def var_np(seq):
    return np.var(seq)

# Definindo os dicionários que receberão os resultados

lista_media_mao = {'1' : [], '2' : [], '3.2' : [], '3.5' : [], '4' : []}
lista_var_mao = {'1' : [], '2' : [], '3.2' : [], '3.5' : [], '4' : []}
lista_media_np = {'1' : [], '2' : [], '3.2' : [], '3.5' : [], '4' : []}
lista_var_np = {'1' : [], '2' : [], '3.2' : [], '3.5' : [], '4' : []}

# Esses dicionários receberão as diferenças entre os valores para análise posterior
lista_media_dif = {'1' : [], '2' : [], '3.2' : [], '3.5' : [], '4' : []}
lista_var_dif = {'1' : [], '2' : [], '3.2' : [], '3.5' : [], '4' : []}




# ++++++++Testes++++++++

for a in lista_a:
    for n in range(1,N):
        seq.append((a*seq[n-1])*(1-seq[n-1]))
    
    lista_media_mao[str(a)] = float(media_mao(seq))
    lista_var_mao[str(a)] = float(var_mao(seq))
    lista_media_np[str(a)] = float(media_np(seq))
    lista_var_np[str(a)] = float(var_np(seq))
    lista_media_dif[str(a)] = float(abs(media_mao(seq) - media_np(seq)))
    lista_var_dif[str(a)] = float(abs(var_mao(seq) - var_np(seq)))

print('medias')
print(f'Media com o codigo na mao: {lista_media_mao}')
print(f'Media com numpy: {lista_media_np}\n')

print('Variancia')
print(f'Variancia com o codigo na mao: {lista_var_mao}')
print(f'Variancia com numpy: {lista_var_np}\n')

print('Diferenca absoluta entre os valores calculados')
print(f'Diferenca para a media: {lista_media_dif}')
print(f'Diferenca para a variancia: {lista_var_dif}')











