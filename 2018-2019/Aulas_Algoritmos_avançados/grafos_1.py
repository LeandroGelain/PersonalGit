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

    def inserir_aresta(self, matriz):
        v1 = int(input('Informe o valor de v1: '))
        v2 = int(input('Informe o valor de v2: '))
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
                if j == 1:
                    try:
                        print(self.array_alface[alfaContColuna],self.array_alface[alfaContLinha])
                    except IndexError:
                        print('Lista fora do range')
                alfaContColuna+=1
            alfaContColuna=0
            alfaContLinha+=1

# ============= codigo novo ==================
#  Trasformar para funcionar na class
# ============================================


    def funcao_verifica(matriz):
        self.array_arestas = []
        cont_letra_linha=0
        cont_letra_coluna=0
        dict_conc = {}
        cont_dict = 0
        for i in matriz:
            for j in i:
                if j == 1:
                    dict_conc = {
                                'vLinha':self.array_alfabeto[cont_letra_linha],
                                'vColuna':self.array_alfabeto[cont_letra_coluna]
                                }
                    self.array_arestas.append(dict_conc)
                cont_letra_coluna+=1
            cont_letra_coluna=0        
            cont_letra_linha+=1
        print('-----------')
        
        self.a_max = []
        a_min = []
        
        for filtra in self.array_arestas:
            a_min.append(filtra['vLinha'])
            a_min.append(filtra['vColuna'])
            self.a_max.append(a_min)
            a_min = []
        print(self.a_max)
        
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