# -*- encoundig: utf-8 -*-

class buscar(object):

    def __init__(self):
        pass    
    
    @classmethod
    def get_no(self):   
        self.no = int(input('Digite o nó de inicio: '))
        return self.no
    @classmethod
    def por_largura(self,adj):
        fila = [self.no]
        visitados = [self.no]

        while len(fila):
            no_retirado = fila.pop(0)
            for vizinho in adj[no_retirado]['adjacentes']:
                if vizinho not in visitados:
                    visitados.append(vizinho)
                    fila.append(vizinho)
        print(visitados)

    @classmethod
    def por_profundidade(self, grafo, vertice, visitados):
        if vertice in visitados:
            return False
        visitados.append(vertice)
        for vizinho in grafo[vertice]['adjacentes']:
            if vizinho not in visitados:
                self.por_profundidade(grafo, vizinho, visitados)
        
        return list(visitados)

grafo_arvore = [
                    {'vertice':0 ,'adjacentes':[1,2]},
                    {'vertice':1 ,'adjacentes':[0,3,4]},
                    {'vertice':2 ,'adjacentes':[0,5,6]},
                    {'vertice':3 ,'adjacentes':[1]},
                    {'vertice':4 ,'adjacentes':[1]},
                    {'vertice':5 ,'adjacentes':[2]},
                    {'vertice':6 ,'adjacentes':[2]}                                
                                                    ]

grafo_orientado = [
                    {'vertice':0 ,'adjacentes':[1,3]},
                    {'vertice':1 ,'adjacentes':[3,4]},
                    {'vertice':2 ,'adjacentes':[0,5]},
                    {'vertice':3 ,'adjacentes':[2,4,5,6]},
                    {'vertice':4 ,'adjacentes':[6]},
                    {'vertice':5 ,'adjacentes':[]},
                    {'vertice':6 ,'adjacentes':[5]} 
                                                    ]

buscar = buscar()
# -----------------------------------------------------------
# buscar.get_no()
# buscar.por_largura(grafo_arvore)
# buscar.get_no()
# buscar.por_largura(grafo_orientado)
# -----------------------------------------------------------
# -----------------------------------------------------------

no = buscar.get_no()

visitados =[]
buscar.por_profundidade(grafo_arvore, no, visitados)
print('grafo em arvore não orientado: ',visitados)

visitados =[]
buscar.por_profundidade(grafo_orientado, no, visitados)
print('Grafo orientado: ',visitados)
# -----------------------------------------------------------
