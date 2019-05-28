'''
Nome do autor: Ilton Batista da Silva Júnior
Data de criação do arquivo: 26/05/2019
Objetivo sucinto do programa: Introdução a python e conceitos basicos
Referência ao enunciado/origem do exercício: https://www.udemy.com/intro_python/learn/lecture/11785586#overview
'''

# -*- coding: utf-8 -*-

#Criação de arquivo
#Se abrir ja um existente vai sobescrever
#Usando o metodo "a" pode adicionar sem sobescrever 
criar_arquivo = open("arquivo.txt", "a")

#Escrever dentro do arquivo 2
criar_arquivo.write("\nEAIIII BROOOOWWW")

#Fechar arquivo
criar_arquivo.close()