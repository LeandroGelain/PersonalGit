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
    
    
matriz_trocada = [
                    [0,1,0,0,1],
                    [1,0,1,1,0],
                    [0,1,0,1,0],
                    [0,1,1,0,1],
                    [1,0,0,1,0]
                                  ]

arestas = funcao_verifica(matriz_trocada)
# imprime_adj(arestas)