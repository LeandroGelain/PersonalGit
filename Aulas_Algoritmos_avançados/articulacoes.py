# -*- encoundig: utf-8 -*-

class buscar(object):

	def por_profundidade(self, grafo, vertice, visitados):
		if vertice in visitados:
			return False
		visitados.append(vertice)
		try:
			for vizinho in grafo[vertice]['adjacentes']:
				if vizinho not in visitados:
					self.por_profundidade(grafo, vizinho, visitados)
			return list(visitados)
		except IndexError:
			pass

	def profundidade_main(self, grafo):
		componentes = []
		visitados = []
		
		for i in range(len(grafo)):
			componente = self.por_profundidade(grafo, i, visitados)
			if not componente == False:
				componentes.append(componente)

			if len(componentes) > 1:
				for rm in componentes[0]:
					if rm in componentes[1]:
						componentes[1].remove(rm)

		return list(componentes)

	def articulation(self, grafo, vertice):
		poped = grafo.pop(0)
		listaComponentes = self.profundidade_main(grafo)
		grafo.append(poped)
		
		if len(listaComponentes)>=2:
			return vertice
	

	def aticulation_main(self, grafo):
		lista_articulacao = []
		
		for vertice in range(len(grafo)):
			articulacao = self.articulation(grafo, vertice)
			lista_articulacao.append(articulacao)
		
		return list(lista_articulacao)

grafo_A = [
	{'vertice':0 , 'adjacentes': [1,2] },
	{'vertice':1 , 'adjacentes': [0,2,3,4]},
	{'vertice':2 , 'adjacentes': [0,1]},
	{'vertice':3 , 'adjacentes': [1]},
	{'vertice':4 , 'adjacentes': [1,5,6]},
	{'vertice':5 , 'adjacentes': [4,6]},
	{'vertice':6 , 'adjacentes': [4,5]}
											]

grafo_B = [

	{'vertice':0 , 'adjacentes': [5,6] },
	{'vertice':1 , 'adjacentes': [4]},
	{'vertice':2 , 'adjacentes': [5,6,9]},
	{'vertice':3 , 'adjacentes': [7,8]},
	{'vertice':4 , 'adjacentes': [1,9]},
	{'vertice':5 , 'adjacentes': [0,2]},
	{'vertice':6 , 'adjacentes': [0,2,4]},
	{'vertice':7 , 'adjacentes': [3,8] },
	{'vertice':8 , 'adjacentes': [3,7,9]},
	{'vertice':9 , 'adjacentes': [2,4,8]}
]

buscar = buscar()
arti_f = buscar.aticulation_main(grafo_B)

articulacoes = list(filter(None, arti_f))
print(f'Articulações: {articulacoes}')

