'''
Nome do autor: Ilton Batista da Silva Júnior
Data de criação do arquivo: 26/05/2019
Objetivo sucinto do programa: Introdução a python e conceitos basicos
Referência ao enunciado/origem do exercício: https://www.udemy.com/intro_python/learn/lecture/11785586#overview
'''

#coding: utf-8

a = 2
b = 3

nomes = ['Pedro', 'Joao', 'Leticia']

contador = 0

print("a = ", a,"\n")
print("b = ", b,"\n")
print("Contador = ", contador)
print("nomes = ", nomes,"\n")

for i in nomes:
    print(i)

print("-----------------------------------------")

for i in range(a):
    print(i)

print("-----------------------------------------")

for i in range(b):
    print(i)

print("-----------------------------------------")

while contador < 5:
    print(contador)
    contador = contador + 1