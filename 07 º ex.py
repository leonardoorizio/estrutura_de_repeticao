#Faça um programa que leia 5 números e informe o maior número.

def comparacao():

    totalizador = 1
    numero = []

    while totalizador <= 5:

        numero.append(input('Entre com um nº:'))
        totalizador += 1

    print(max(numero))

comparacao()