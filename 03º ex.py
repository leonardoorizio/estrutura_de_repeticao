#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


def nome():

    nome = input('Nome:')
    validador_nome = len(nome)

    while validador_nome > 3:
        print('Número maximo de caracteres que são 3, tente novamente!')
        nome = input('Nome:')
        validador_nome = len(nome)

    print('ok')

def idade():

    idade = int(input('Idade:'))

    while (idade < 0) or (idade > 150):
        print('Idade deve estar dentro de 0 a 150, tente novamente!')
        idade = int(input('Idade:'))

    print('ok')

def salario():

    salario = float(input('Salário:'))

    while salario < 0:
        print('Salario deve ser maior que zero, tente novamente!')
        salario = float(input('Salário:'))

    print('ok')

def sexo():

    sexo = str.upper( input ('Sexo:'))

    while (sexo != 'F') and (sexo != 'M'):
        print('Gênero inválido, tente novamente!')
        sexo = input('Sexo:')

    print('ok')

def estado_civil():

    estado_civil = str.upper(input('Estado civil (S,C,V,D):'))
    lista = ['S','C','V','D']

    while estado_civil not in lista:

        print('Desculpe, opção inválida. Tente novamente!')
        estado_civil = str.upper(input('Estado civil (S,C,V,D):'))

    print('ok')

nome()
idade()
salario()
sexo()
estado_civil()

print('\nResumo do cadastro:\n')
print(f'Nome: {nome}.\n')
print(f'Idade: {idade}.\n')
print(f'Salário: R${salario}.\n')
print(f'Sexo: {sexo}.\n')
print(f'Estado civil: {estado_civil}.\n')




