class Calculadora(object):
    def __init__(self):
        print('Calculadora iniciada')
        print('--------------------')
        
    
    def soma(self, numero1, numero2):
        self.resultado = numero1+numero2
        return self.resultado
    
    def subtrai(self, numero1,numero2):
        self.resultado = numero1-numero2
        return self.resultado
    
    def multiplica(self, numero1, numero2):
        self.resultado = numero1*numero2
        return self.resultado
    
    def dividi(self, numero1, numero2):
        self.resultado = numero1/numero2
        return self.resultado
    
c = Calculadora()

print(c.soma(3,4))
print(c.subtrai(3,4))
print(c.multiplica(3,4))
print(c.dividi(12,2))
