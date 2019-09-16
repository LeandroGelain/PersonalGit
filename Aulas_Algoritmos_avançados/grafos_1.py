class Graph_matriz(object):
    def __init__(self, num_vertices):
        self.n_vertices = num_vertices
        self.array_alfabeto = ['a','b','c','d','e','f','g','h']
    
    def armazena(self):
        self.matriz = []
        for i in range(self.n_vertices):
            self.matriz.append([])
            for j in range(self.n_vertices):
                self.matriz[i].append(0)

        return self.matriz

    def inserir_aresta(self, matriz, v1, v2):
        linha=0
        coluna=0
        self.matriz = matriz
        for i in matriz:
            for j in i:
                if (linha == v1 and coluna == v2):
                    self.matriz[v1][v2] = 1
                elif (linha == v2 and coluna == v1):
                    self.matriz[v2][v1] = 1
                coluna+=1
            coluna=0
            linha+=1
        return self.matriz

    def printa_matriz(self, matriz):
        for m in matriz:
            print(m)

    def verifica_adj(self, matriz, vertice):
        alfaContLinha=0
        alfaContColuna=0

        for i in matriz:
            for j in i:
                # print(j)
                # print('Vetor coluna',self.array_alface[alfaContColuna])
                if j == 1:
                    try:
                        print(self.array_alface[alfaContColuna],self.array_alface[alfaContLinha])
                    except IndexError:
                        print('Lista fora do range')
                alfaContColuna+=1
            # print('Vetor linha',self.array_alface[alfaContLinha])
            
            alfaContColuna=0
            alfaContLinha+=1

    # ============= codigo novo ==================
def funcao_verifica(matriz):
    array_alfabeto = ['a','b','c','d','e','f','g','h']
    array_arestas = []
    cont_letra_linha=0
    cont_letra_coluna=0
    dict_conc = {}
    cont_dict = 0
    for i in matriz:
        # print(i, array_alfabeto[cont_letra_linha])
        for j in i:
            # print(i[j],array_alfabeto[cont_letra_coluna])
            if j == 1:
                dict_conc = {
                            'vLinha':array_alfabeto[cont_letra_linha],
                             'vColuna':array_alfabeto[cont_letra_coluna]
                             }
                array_arestas.append(dict_conc)
                # print('um aqui', array_alfabeto[cont_letra_linha],array_alfabeto[cont_letra_coluna])
            cont_letra_coluna+=1
        cont_letra_coluna=0        
        cont_letra_linha+=1
    print('-----------')
    # print(array_arestas[0])
    
    a_max = []
    a_min = []
    
    for filtra in array_arestas:
        a_min.append(filtra['vLinha'])
        a_min.append(filtra['vColuna'])
        a_max.append(a_min)
        a_min = []
    print(a_max)
    cont_compara_p = 0
    cont_compara_s = 0
    while True:
        if a_max[cont_compara_p][cont_compara_s] == a_max[cont_compara_p][cont_compara_s]:
            print(a_max[cont_compara_p]) 
            cont_compara_p+=1
        else:
            cont_compara_s+=1   
    # return arestas
    
def imprime_adj(matriz_arestas):
    for i in matriz_arestas:
        splita_i = i.split(' ')
        print('Vertice {} tem como adjacencia o vertice {}.'.format(splita_i[0],splita_i[1]))
    

# vertices = int(input('Digite o numero de vertices (v <= 8): '))
g = Graph_matriz(0)

matriz_trocada = [[0,1,0,0,1],
                  [1,0,1,1,0],
                  [0,1,0,1,0],
                  [0,1,1,0,1],
                  [1,0,0,1,0]]

g.verifica_adj(matriz_trocada, 3)

quit()

# if __name__ == '__main__':
#     matriz = g.armazena()
#     # g.printa_matriz(matriz)
#     print('---------------------------')
#     while True:
#         v1 = int(input('digite o vertice v1: '))
#         v2 = int(input('digite o vertice v2: '))
#         try:
#             matriz_trocada = g.inserir_aresta(matriz, v1, v2)
#             resposta = str(input('Quer acrecentar mais? '))
#             while True:
#                 if resposta.lower == 'sim':
#                     v1 = int(input('digite o vertice v1: '))
#                     v2 = int(input('digite o vertice v2: '))
#                     matriz_trocada = g.inserir_aresta(matriz, v1, v2)
#                 else:
#                     pass
#                 break
#             break
#         except IndexError:
#             print('Lista fora do range')
#     g.printa_matriz(matriz_trocada)
#     print('---------------------------')

    