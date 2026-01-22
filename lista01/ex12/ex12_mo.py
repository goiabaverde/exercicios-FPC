import numpy as np
import matplotlib.pyplot as plt

def cria_grafo():
    return {'coord' : {}, 'adj' : {} }

def remove_no(G: dict, u: int):
    if u not in G['coord']:
        raise("Erro: esse nó não existe, logo não pode ser removido")
    for w in list(G['adj'].get(u)):
        G['adj'][w].discard(u)
    
    G['adj'].pop(u)
    G['coord'].pop(u)

def remove_aresta(G : dict, u : int, v :int, remover_isolado = True):
    if u in G['adj'][v] and v in G['adj'][u]:
        G['adj'][u].discard(v)
        G['adj'][v].discard(u)
    if remover_isolado:
        if u in G['coord'] and len(G['adj'].get(u)) == 0:
            remove_no(G, u)
        if v in G['coord'] and len(G['adj'].get(v)) == 0:
            remove_no(G, v)

    else:
        print('Nós isolados podem permanecer na estrutura de grafo')
        

def plota_grafo(G : dict, tam_mk = 200, title = 'Grafo'):
    fig, ax = plt.subplots(figsize = (10,9))
    coord = G['coords']

    for u in coord:
        x1, y1 = coord[u]
        for v in G['adj'].get(u):
            pass
            




