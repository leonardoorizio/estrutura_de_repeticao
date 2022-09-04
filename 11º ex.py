#Altere o programa anterior para mostrar no final a soma dos números.

def validador_impar():

    a = int(input("Entre com um número: "))
    b = int(input("Entre com um número: "))

    while b < a:

        a = int(input("Entre com um número: "))
        b = int(input("Entre com um número: "))

    else:

        for i in range(a,b,1):
            print(i)

    print(f'Soma dos números: {a+b}')

validador_impar()