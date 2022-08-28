#Faça um programa que leia 5 números e informe a soma e a média dos números.

import numpy

def comparacao():

    totalizador = 1
    numero = []

    while totalizador <= 5:

        numero.append(int(input('Entre com um nº:')))
        totalizador += 1

    print(f'\nSoma:{sum(numero)}')
    print(f'\nMédia:{numpy.mean(numero)}')

comparacao()