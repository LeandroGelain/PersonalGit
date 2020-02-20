import random
class Hamming(object):
    def __init__(self):
        pass

    @classmethod
    def number_to_binary(self, numero):
        self.Bytes = ("{0:b}".format(numero))
        self.array_bits = []
        for self.bit in self.Bytes:
            self.array_bits.append(int(self.bit))
        return list(self.array_bits)
    
    @classmethod
    def error_bit(self, array_bits):
        print('===============================')
        print('Array certo: ',array_bits)
        self.random_position = random.randint(0,len(array_bits)-1)
        print('Posição alterada',self.random_position)
        if array_bits[self.random_position] == 0:
            array_bits[self.random_position] = 1
        elif array_bits[self.random_position] == 1:
            array_bits[self.random_position] = 0
            
        print('Array com erro',array_bits)
        print('===============================')
        return list(array_bits)  

    @classmethod    
    def indices(self, p, tamanho):
        for i in range(p,tamanho+1,p*2):
            yield from range(i,min(i+p,tamanho+1))

    @classmethod
    def main(self):
        numero = int(input('Numero pra binario:'))
        list_bits = self.number_to_binary(numero)
        list_err = self.error_bit(list_bits)
        cont=1
        lista_ps=[1,2,4,8,16]
        for i in lista_ps:
            if len(list_bits) >= i:
                print(i)

array = [0,1,2,3,4,5,6,7]

if __name__ == '__main__': 
    Hamming.main()