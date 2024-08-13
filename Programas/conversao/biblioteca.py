from time import sleep

def metade(valor):
    resultado = valor / 2
    return f'A metade de R$ \033[1;33m{valor:.2f}\033[m é R$ \033[1;34m{resultado:.2f}\033[m'


def dobro(valor):
    resultado = valor * 2
    return f'O dobro de R$ \033[1;33m{valor:.2f}\033[m é R$ \033[1;34m{resultado:.2f}\033[m'


def dezporcentomais(valor):
    resultado = valor + (valor * 10/100)
    return f'Aumentando 10% de R$ \033[1;33m{valor:.2f}\033[m, temos R$ \033[1;34m{resultado:.2f}\033[m'


def dezporcentomenos(valor):
    resultado = valor - (valor * 13/100)
    return f'Diminuindo 13% de R$ \033[1;33m{valor:.2f}\033[m, temos R$ \033[1;34m{resultado:.2f}\033[m'
    

def convertersinal(valor):
    return valor.replace('.', ',')


def virgula(moeda):
    valido = False
    while not valido:
        entrada = str(input(moeda)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def programa(valor):
    print('\033[1;32m=\033[m' * 60)
    moeda = virgula('Digite o preço: R$ ')
    print('\033[1;32m=\033[m' * 60)
    sleep(.3)
    print(convertersinal(metade(moeda)))
    sleep(.3)
    print(convertersinal(dobro(moeda)))
    sleep(.3)
    print(convertersinal(dezporcentomais(moeda)))
    sleep(.3)
    print(convertersinal(dezporcentomenos(moeda)))
    sleep(.3)
    return valor
