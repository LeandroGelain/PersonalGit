class Graph_matriz(object):
    def __init__(self, num_vertices):
        self.n_vertices = num_vertices
        self.array_alface = ['a','b','c','d','e','f','g','h']
    
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

    