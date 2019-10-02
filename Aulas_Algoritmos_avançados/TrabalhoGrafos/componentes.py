# -*- encoundig: utf-8 -*-

class buscar(object):

	def por_profundidade(self, grafo, vertice, visitados):
			if vertice in visitados:
    				return False
			visitados.append(vertice)
			for vizinho in grafo[vertice]['adjacentes']:
				if vizinho not in visitados:
					self.por_profundidade(grafo, vizinho, visitados)
			return list(visitados)

grafo = [
	# componente 1
	{'vertice':0 , 'adjacentes': [1,2] },
	{'vertice':1 , 'adjacentes': [0,3,4]},
	{'vertice':2 , 'adjacentes': [0,5,6]},
	{'vertice':3 , 'adjacentes': [1]},
	{'vertice':4 , 'adjacentes': [1]},
	{'vertice':5 , 'adjacentes': [2]},
	{'vertice':6 , 'adjacentes': [2]},

	# componente 2    
	{'vertice':7 , 'adjacentes': [8,10]},
	{'vertice':8 , 'adjacentes': [7,9,10]},
	{'vertice':9 , 'adjacentes': [11]},
	{'vertice':10 , 'adjacentes': [7,8]},
	{'vertice':11 , 'adjacentes': [8,9]}
						]

buscar = buscar()

componentes = []
visitados = []
for i in range(0,len(grafo)):
    componente = buscar.por_profundidade(grafo, i, visitados)
    if not componente == False:
        componentes.append(componente)

for rm in componentes[0]:
    componentes[1].remove(rm)

for c in range(len(componentes)):
	print('Componente %s: %s'%(c+1,componentes[c]))
