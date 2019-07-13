import math

class ObjetoGrafico(object):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno):
        self.cor_de_preenximento = cor_de_preenximento
        self.cor_de_contorno = cor_de_contorno
        self.preenxida = preenxida
        
    
    def area(self , base, altura):
        self.resultado = base*altura
        return self.resultado
    
    def perimetro(self, base, altura):
        self.resultado = (base*2)+(altura*2)
        return self.resultado
    
class Retangulo(ObjetoGrafico):
    def __init__(self,cor_de_preenximento, preenxida, cor_de_contorno):
        super(Retangulo, self).__init__(cor_de_preenximento, preenxida, cor_de_contorno)
      
    def area(self, base, altura):
        return super(Retangulo, self).area(base, altura)
    
    def perimetro(self, base, altura):
        return super(Retangulo, self).perimetro(base, altura)

class Triangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno):
        super(Triangulo, self).__init__(cor_de_preenximento, preenxida, cor_de_contorno)
    
    def area(self, base, altura):
        self.resultado = (base*altura)/2
        return self.resultado

    def perimetro(self, base, altura):
        self.Meiabase = base/2
        self.hipo = math.sqrt(math.pow(self.Meiabase,2)+math.pow(altura,2)) 
        self.resultado =  (self.hipo*2)+base
        return self.resultado

class Circulo(ObjetoGrafico):
    def __init__(self, cor_de_preeximento, preenxiada, cor_de_contorno):
        super(Circulo, self).__init__(cor_de_preeximento, preenxiada, cor_de_contorno)

    def area(self, raio):
        self.resultado = math.pi*math.pow(raio,2)
        return self.resultado
    
    def perimetro(self, raio):
        self.resultado = math.pi*(raio*2)
        return float(self.resultado)

# -------------------------------------------------
# Chamando objetos e metodos
    
print('-------- Retangulo --------')
retangulo = Retangulo('Azul', True, 'Preto')
resultadoAreaRetangulo = retangulo.area(4, 20)
resultadoPerimetroRetangulo = retangulo.perimetro(4, 20)

print('Area: ',resultadoAreaRetangulo)
print('Perimetro: ',resultadoPerimetroRetangulo)
print('-----------------------------\n')

print('-------- Trinagulo --------')
triangulo = Triangulo('azul', True , 'Verde')
resultadoAreaTriangulo = triangulo.area(6,4)
resultadoPerimetroTriangulo = triangulo.perimetro(6,4)

print('Area: ',resultadoAreaTriangulo)
print('Perimetro: ',resultadoPerimetroTriangulo)
print('-----------------------------\n')

print('-------- Circulo --------')
circulo = Circulo('Vermelho', True, 'Preto')
resultadoAreaCirculo = circulo.area(4)
resultadoPerimetroCirculo = circulo.perimetro(4)

print('Area: %.2f'%resultadoAreaCirculo)
print('Perimetro: %.2f'%resultadoPerimetroCirculo)
print('-----------------------------\n')