#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def impar():

    a = 1
    b = 0

    while b < 50:
        if (a % 2) != 0:
            print(a)
            a += 1
            b += 1
        else:
            a += 1
            b += 1

impar()