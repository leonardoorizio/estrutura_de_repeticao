#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def impares():

    i = 1

    while i <= 50:
        if i % 2 != 0:
            print(i)
            i += 1
        else:
            i += 1

impares()