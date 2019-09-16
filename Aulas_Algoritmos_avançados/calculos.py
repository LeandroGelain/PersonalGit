class calcular(object):

    def __init__(self):
        pass
    
    @classmethod
    def fatorial(self, numero):
        if numero == 0:
            return 1
        return numero * self.fatorial(numero-1)

    @classmethod
    def fibonacci(self, numero_elemento):
        if numero_elemento <= 2:
            return 1
        return self.fibonacci(numero_elemento-1) + self.fibonacci(numero_elemento-2) 

    @classmethod
    def multiplica(self, x, y):
        if y == 1:
            return x
        return x + self.multiplica(x,y-1)

    @classmethod
    def eleva(self, x, y):
        if y ==1:
            return x
        return x * self.eleva(x,y-1)
    @classmethod
    def somatoria(self,x):
        if x == 1:
            return x
        return x + self.somatoria(x-1)

    @classmethod
    def primeiro_algarismo(self, num):
        if 10 > num > 0:
            return num
        return self.primeiro_algarismo(int(num/10))

    @classmethod
    def tira_numero(self, lista,num):
        if num != lista:
            return lista
        else:
            lista = lista.remove(num)
            return self.tira_numero(lista,num)

num = int(input('Numero pra tirar: '))
lista = [1,1,1,2,3,4,5,6]
resultado = calcular.tira_numero(lista,num)
print(resultado)