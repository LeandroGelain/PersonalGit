r = 'sim'
while r == 'sim':
    print('-='*20)
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    
    #delta
    print('-='*20)
    if a == 0:
        print('Isso não é função do segundo grau.')
        break
    elif a > 0:
        print('A função é crescente.')
    elif a < 0: 
        print('A função é decrescente.')
    delta = (b**2)-(4*a*c)
    if delta < 0:
        print('Delta e menor que zero')
        break
    print('Delta é igual a {}'.format(delta))
    print('-='*20)
    
    #raiz    
    raiz1 = (-b + delta**0.5)/(2*a)
    raiz2 = (-b - delta**0.5)/(2*a)
    
    print (raiz1)
    print (raiz2)

    if raiz1 == raiz2:
        print('As raizes são iguais.')

    elif raiz1 != raiz2:
        print('As raizes são difentes.')

    elif raiz1 < 0:
        print('A raiz não é real')
    
    elif raiz2 < 0:
        print('A raiz não é real')
    
    elif delta == 0:
        print('Delta e igual a zero')
    
    #vertices

    Vxv = -b/(2*a)
    Vyv = -delta/(4*a)   

    print('O vertice Xv é {}'.format(Vxv))
    print('O vertice Yv é {}'.format(Vyv))
    print('O intecepto é (0,{})'.format(c))
    r = str(input('Quer continuar? [sim/nao]'))
    print('-='*20)