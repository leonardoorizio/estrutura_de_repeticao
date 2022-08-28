#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def nota():

    cliente = int(input('Nos de uma nota de 0 a 10, para que possamos melhorar ainda mais sua experiência:'))

    while cliente < 0 or cliente > 10:
        print('Desculpe, valor invalido. Digite novamente!')
        cliente = int(input('Nos de uma nota de 0 a 10, para que possamos melhorar ainda mais sua experiência:'))

    print('Obrigado, volte sempre!')

nota()