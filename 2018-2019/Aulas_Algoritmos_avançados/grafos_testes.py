def funcao_verifica(matriz):
    array_alfabeto = ['a','b','c','d','e','f','g','h']
    array_arestas = []
    cont_letra_linha=0
    cont_letra_coluna=0
    dict_conc = {}
    cont_dict = 0
    for i in range(0,len(matriz)):
        for j in range(i+1):
            if matriz[i][j] == 1:
                dict_conc = {
                            'vLinha':array_alfabeto[cont_letra_linha],
                             'vColuna':array_alfabeto[cont_letra_coluna]
                             }
                array_arestas.append(dict_conc)
            cont_letra_coluna+=1
        cont_letra_coluna=0        
        cont_letra_linha+=1
    print('-----------')
    
    a_max = []
    a_min = []
    
    for filtra in array_arestas:
        a_min.append(filtra['vLinha'])
        a_min.append(filtra['vColuna'])
        a_max.append(a_min)
        a_min = []
    print(a_max)

    
# def imprime_adj(matriz_arestas):
#     for i in matriz_arestas:
#         splita_i = i.split(' ')
#         print('Vertice {} tem como adjacencia o vertice {}.'.format(splita_i[0],splita_i[1]))
    
    
matriz_trocada = [
                    [0,1,0,0,1],
                    [1,0,1,1,0],
                    [0,1,0,1,0],
                    [0,1,1,0,1],
                    [1,0,0,1,0]
                                  ]

arestas = funcao_verifica(matriz_trocada)
# imprime_adj(arestas)
