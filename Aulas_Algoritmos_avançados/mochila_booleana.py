import math

class Mochila():
	
	def __init__(self,lista,capacidade):
		self.lista=lista
		self.capacidade=capacidade
		self.cont=0
		self.itens=[ False ]*len(lista)

	def solve(self):
		matriz_n = len(self.lista)
		matriz_W = self.capacidade
		V = [[0]*(matriz_W+1) for i in range(matriz_n+1)]
		tabela_troca = [[False]*(matriz_W+1) for i in range(matriz_n+1)]
		for i in range(1,matriz_n+1):
			for j in range(1,matriz_W+1):
				pesoI=self.lista[i-1]['peso']
				if pesoI > j:
					V[i][j] = V[i-1][j]
					self.cont+=1
				else:
					V[i][j] = max(V[i-1][j-pesoI]+self.lista[i-1]['valor'],V[i-1][j])
					if V[i-1][j-pesoI]+self.lista[i-1]['valor'] > V[i-1][j]:
						tabela_troca[i][j] = True
					self.cont+=1
		for i in range(matriz_n, 0, -1):
			if tabela_troca[i][matriz_W]:
				self.itens[i-1] = True
				matriz_W-=self.lista[i-1]['peso']
			else:
				self.itens[i-1] = False
		return V

if __name__ == "__main__":

	itens_list = [
			 {'item':1,'peso':12,'valor':4},
			 {'item':2,'peso':1,'valor':2},
			 {'item':3,'peso':1,'valor':1},
			 {'item':4,'peso':4,'valor':10},
			 {'item':5,'peso':2,'valor':2}
			]

	mochila = Mochila(itens_list,15)
	mochila.solve()
	print ("Itens na mochila: ")
	for i in range(len(mochila.itens)):
		if mochila.itens[i]:
			print ("Item: %s Peso: %s Valor %s" % (mochila.lista[i]['item'],mochila.lista[i]['peso'],mochila.lista[i]['valor']))