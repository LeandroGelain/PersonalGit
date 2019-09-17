def caminho_hamiltoniano(grafo, size, ponto, path=[]):
    if ponto not in set(path):
        path.append(ponto)
        if len(path) == size:
            return path
        todos_candidatos = []
        for prox_ponto in grafo.get(ponto, []):
            res_path = [i for i in path]
            candidatos = caminho_hamiltoniano(grafo, size, prox_ponto, res_path)
            if candidatos is not None:  
                todos_candidatos.extend(candidatos)
            else:
                pass
        return todos_candidatos
    else:
        return None


if __name__ == '__main__':
    ponto = 1
    size = 4

    grafo = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
    
    grafo2 = {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
    
    grafo3 = {0:[1,2],1:[3,4],2:[0,5,6],3:[1],4:[1],5:[2],6:[2]}

    path = caminho_hamiltoniano(grafo, size, ponto)
    lista_candidados = []
    for j in range(size):
        while j*size < len(path):
            start = int(j*size)
            end = int((j+1)*size)
            lista_candidados.append(path[start:end])
            break
    print('Candidatos a ciclos hamiltonianos: '%(lista_candidados))

    if len(lista_candidados) == 0:
        print('Não há caminho hamiltoniano, então, não há ciclo hamiltoniano')
    else:
        for candidato in lista_candidados:
            if ponto in grafo[candidato[-1]]:
                print('O caminho %s é um ciclo hamiltoniano'%(candidato))
            else:
                print('O caminho %s não é um ciclo hamiltoniano'%(candidato))