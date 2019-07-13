class Banco(object):
    
    __total = 10000
    __reservaExigida = 100
    TaxaReserva = 0.1
    
    def __init__(self, saldo):
        self.saldo = saldo
        print('Inicialize Bank')
        
    def __CalcularReserva(self, __total, TaxaReserva):
        self.reserva = Banco.__total*Banco.TaxaReserva
        return self.reserva
    
    def podeFazerEmprestimo(self, valorEmprestimo):
        if valorEmprestimo > Banco.__total-Banco.__reservaExigida:
            print('Não pode fazer o emprestimo')
            return False
        else:
            # print('Pode fazer o emprestimo')
            return True
        print(Banco.__CalcularReserva())
        
class Conta(object):
    
    def __init__(self, __saldo, __ID, __senha):  
        self.__saldo = __saldo
        self.__ID = __ID
        self.__senha = __senha
    
    def deposito(self, __senha, valor):
        if __senha == 123:
            self.__saldo += valor
            print('Saldo atual da conta: %s'%self.__saldo)
        else:
            print('Senha incorreta')
    
    def saque(self, __senha, valor):
        if __senha == 123:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print('Seu saldo atual é de %s '%self.__saldo)
            else:
                print('Valor alto d+')
        else:
            print('Senha incorreta, tente novamente')
            
    def podeReceberEmprestimo(valor):
        if Banco.podeFazerEmprestimo(itau,50000) == True:
            print('Pode receber emprestimo!')
            return True
        else:
            print('Não pode receber emprestimo')
            return False
    
    def saldo(self):
        self.saldo = self.__saldo
        print(self.saldo)
        
itau = Banco(4000)
itau = itau.podeFazerEmprestimo(8000)


eu = Conta(5000, 123 , 123)
eu.saque(123,3000)
(eu.saldo())