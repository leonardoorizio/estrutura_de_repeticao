#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

def tabuada():

    cliente = int(input('Entre com número para saber a Tabuada:'))

    tabuada = [1,2,3,4,5,6,7,8,9,10]

    for i in tabuada:
        resultado = (cliente * i)
        print(f'{cliente } x { i} = {resultado}')

tabuada()
