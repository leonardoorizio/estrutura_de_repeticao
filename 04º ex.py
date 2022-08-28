#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.

def populacao():

    populacao = 80000
    taxa_de_crescimento = 3
    b = 200000
    totalizador = 0

    while (populacao < b):

        populacao += (populacao / 100) * taxa_de_crescimento
        totalizador += 1
        print(f'\nPopulação:', round(populacao))

    print(f'\nTotal de habitantes {round(populacao)}, total de anos: {totalizador}.')

populacao()