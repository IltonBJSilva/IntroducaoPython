'''
Nome do autor: Ilton Batista da Silva Júnior
Data de criação do arquivo: 26/05/2019
Objetivo sucinto do programa: Introdução a python e conceitos basicos
Referência ao enunciado/origem do exercício: https://www.udemy.com/intro_python/learn/lecture/11785586#overview
'''

#coding: utf-8

arquivo = open("arquivo.txt")

#Joga dentro de uma lista
#linhas = arquivo.readlines()


#print(arquivo,"\n\n")
#print(linha)

#Imprimir uma por uma
'''
for linha in linhas:
    print(linha)
'''

#ja vai o texto todo
texto_completo = arquivo.read()

print(texto_completo)