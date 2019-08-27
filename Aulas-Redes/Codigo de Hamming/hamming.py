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
    
    
if __name__ == '__main__':
    numero = int(input('Numero pra binario:'))
    list_bits = Hamming.number_to_binary(numero)
    list_err = Hamming.error_bit(list_bits)
    