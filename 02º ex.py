#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir
#as informações.

def validacao():

        usuario = input('Usuário:')
        senha = input('Senha:')

        while usuario == senha:
            print('Desculpe, Usuário e Senha não pode coincidir. Tente novamente!')
            usuario = input('Usuário:')
            senha = input('Senha:')

        print('Login criado com sucesso :)')

validacao()
