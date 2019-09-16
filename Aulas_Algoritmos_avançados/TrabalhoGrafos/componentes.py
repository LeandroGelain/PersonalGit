import networkx as nx
import matplotlib.pyplot as plt

def buildG(G):
    grafo = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[7,8],[7,10],[8,10],[8,11],[9,11]]
    for arestas in grafo:
        G.add_edge(arestas[0],arestas[1])

def main():
    graph_fn="tempset3.txt";
    G = nx.Graph() 
    buildG(G)
    comps=nx.connected_components(G)
    nx.draw(G)
    plt.show()
    cont=1
    for comp in comps:
        print('Componete %s : %s '%(cont,comp))
        cont+=1
main()