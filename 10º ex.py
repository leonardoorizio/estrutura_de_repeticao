#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles

def validador_impar():

    a = int(input("Entre com um número: "))
    b = int(input("Entre com um número: "))

    while b < a:

        a = int(input("Entre com um número: "))
        b = int(input("Entre com um número: "))

    else:

        for i in range(a,b,1):
            print(i)

validador_impar()