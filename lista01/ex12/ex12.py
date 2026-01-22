import numpy as np
from matplotlib import pyplot as plt

# Inicialiar um dicionário  n elementos, onde esses elementos são tuplas e indicam as coordenas dos vértices desse grafo, o grafo n é identificado pelo seu índice na lista

vertices = {
    0: (4, 5),
    1: (2, 5),
    2: (1, 4),
    3: (1, 2),
    4: (2, 1),
    5: (4, 1),
    6: (4, 3),
    7: (3, 3)
}

#Inicializar uma dicionário chamado de conectividade que indica com quem um vértice está ligado, onde o  key value é o vértice e o value é uma conjunto onde os índices dos vértices os quais esse vértice está ligado estão presentes

conectividade = {
    0: {1},
    1: {0,2},
    2: {1,3},
    3: {2,4},
    4: {3,5},
    5: {4,6},
    6: {5,7},
    7: {6}
}

coord_x = []
coord_y = []


def plotar_grafo(vertices, conectividade):
    for key in vertices.keys():
        if len(conectividade[key]) != 0:
            for elem in conectividade[key]:
                if( not (key  in conectividade[elem])):
                    raise("Esse grafo não está coerente, deve-se checar as conectividades")



    plt.figure(figsize=(6,6))

    plt.title("Representação do grafo")

    for value in vertices.values():
        coord_x.append(value[0])
        coord_y.append(value[1])
    
    plt.scatter(coord_x, coord_y, label="Vértices", color='r')

    
    for key in vertices.keys():
        x_alvos = []
        y_alvos = []
        vertices_alvo = conectividade[key]
        xo = vertices[key][0]
        yo = vertices[key][1]
        if (len(vertices_alvo) != 0):
            for id in vertices_alvo:
                plt.plot([xo,vertices[id][0]], [yo, vertices[id][1]], color = 'b')
        else:
            pass
        # Significa que é um vértice isolado, ele não faz ligação nenhuma



    plt.legend()
    plt.show()

def add_aresta(n1, n2):
    # Checa se existe esses dois vértices para que possam ser adicionados

    if(n1 in vertices and n2 in vertices):
        conectividade[n1].add(n2)
        conectividade[n2].add(n1)

    else:
        raise("Erro, ambos os vértices devem exister")
    
def remove_aresta(n1, n2):
    # Checa se realmente eles estão conectados
    if(n1 in conectividade[n2] and n2 in conectividade[n1]):
        conectividade[n1].remove(n2)
        conectividade[n2].remove(n1)
    else:
        raise("Erro, esses vértices não apresentam arestas os ligando")


    


    

    

plotar_grafo(vertices, conectividade)
add_aresta(2,0)
plotar_grafo(vertices, conectividade)
remove_aresta(0,2)
plotar_grafo(vertices, conectividade)


    
    