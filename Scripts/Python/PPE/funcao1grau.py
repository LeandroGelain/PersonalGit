ax = int(input('Digite o valor de ax: '))
b = int(input('Digite o valor de b: '))

r = b/ax
print('-='*20)
print('A raiz é: {}'.format(r))
print('O intercepto é: (0,{})'.format(b))
if ax == 0:
    print('Isso não é função do primeiro grau.')

elif ax > 0:
    print('A função é crescente.')

elif ax < 0: 
    print('A função é decrescente.')
print('-='*20)

