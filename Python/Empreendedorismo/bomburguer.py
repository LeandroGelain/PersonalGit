def compra_quanto():
    materia_prima = [
                        {"materia":25/16},
                        {"materia":112.3/112},
                        {"materia":58/496},
                        {"materia":48.6/36},
                        {"materia":38.9/224},
                        {"materia":29.4/12}
                                            ]


    caixa = 3212
    cont=0
    while caixa >= 0:
        for i in range(len(materia_prima)):
            caixa = caixa - (materia_prima[i]["materia"])
        print(caixa)
        cont+=1
    print(cont)

def inputa_quanto():
        materia_prima = [
                        {"materia":25.0},
                        {"materia":112.3},
                        {"materia":58.0},
                        {"materia":48.6},
                        {"materia":38.9},
                        {"materia":29.4}
                                            ]

        resultado =   ((materia_prima[0]["materia"]*30)+((materia_prima[1]["materia"])*4)+((materia_prima[2]["materia"])*1)+((materia_prima[3]["materia"])*13)+((materia_prima[4]["materia"])*2)+((materia_prima[5]["materia"])*40))
        print(resultado)
        return resultado

def quanto_de_cada():

    estoque = [178,373,500,155,0,88]
    comprar =       [480,336,496,468,448+224,444+36]
    compra_por_vez = [16,112,496,36,224,12]
    
    for i in range(len(estoque)):
        print(comprar[i]+estoque[i])


quanto_de_cada()