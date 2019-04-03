#-*- encoding: utf-8 -*-
import csv

Arq = open("dados.csv", "a+")                                                                                                                                                                            

r = "s"
while (r == "s"):
	nome = str(input("Digite o nome: "))
	endereco = str(input("Digite o endereço: "))
	cidade =  str(input("digite a cidade: "))
	estado = str(input("digite o estado: "))
	cep =  (input("Digite o cep (sem traços e pontos: "))

	r = str(input("Quer continuar (s/n): "))
	insert = nome + " ; " + endereco + " ; " + cidade + " ; " + estado + " ; " + str(cep)

	Arq.write(insert)

Arq.close()