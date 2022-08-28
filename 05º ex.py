#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def populacao():

    cliente = 'SIM'

    while cliente == 'SIM':

        populacao = float(input('\nPopulação:'))
        taxa_de_crescimento = float(input('Taxa de crescimento:'))
        b = 200000
        totalizador = 0

        while (populacao < b):

            populacao += (populacao / 100) * taxa_de_crescimento
            totalizador += 1
            print(f'\nPopulação:', round(populacao))

        print(f'\nTotal de habitantes {round(populacao)}, total de anos: {totalizador}.')

        cliente = str.upper(input('\nDeseja repetir o processo (SIM/NÃO):'))

populacao()