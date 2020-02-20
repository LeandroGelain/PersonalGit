resultado = 0
resp = 'sim'
while resp == 'sim':
    print('faça sua escolha: ')
    
    print('''
     ____________________________________
    |     Produto     | codigo |  Preço  |
    |_________________|________|_________|
    | Cachorro quente |  100   | R$ 1.20 |
    |   Bauru Simples |  101   | R$ 1.30 |
    |    Bauru Ovo    |  102   | R$ 1.50 |
    |    Hamburguer   |  103   | R$ 1.20 |
    |   CheeseBurguer |  104   | R$ 1.70 |
    |       Suco      |  105   | R$ 2.20 |
    |   Refrigerante  |  106   | R$ 1.00 |
    |_________________|________|_________|
    ''')
    cod = int(input('Digite o codigo: '))
    if cod == 100:
        hotDog = 1.20
        resultado = resultado + hotDog

    elif cod == 101:
        bauruS = 1.30
        resultado = resultado + bauruS

    elif cod == 102:        
        bauruOvo = 1.50
        resultado = resultado + bauruOvo

    elif cod == 103:
        hambu = 1.20
        resultado = resultado + hambu

    elif cod == 104:
        cheesse =1.70
        resultado = resultado + cheesse

    elif cod == 105:    
        suco = 2.20
        resultado = resultado + suco

    elif cod == 106:    
        refri = 1.00
        resultado = resultado + refri

    resp = str(input("Você quer continuar? [sim/não]"))

print ("O valor a ser pago é R${}".format(resultado))