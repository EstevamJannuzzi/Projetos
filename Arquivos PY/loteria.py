from random import randint
from time import sleep

while True:
    texto = 'LOTERIA'
    print('\033[1;34m=\033[m' *50)
    print(f'\033[1;33m{texto:^50}\033[m')
    print('\033[1;34m=\033[m' *50)
    resp = str(input('Vamos jogar?(Sim ou Não): ')).upper()[0]
    if resp == 'S':
        l1 = [randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61)]
        l1.sort()
        
        print('\033[1;34m=\033[m' *50)
        print('\033[1;33mFaça as 6 escolhas de números entre 1 à 60!\033[m')
        print('\033[1;34m=\033[m' *50)
        
        l2 = []
        for contagem in range(0, 6):
            l2.append(int(input(f'{contagem + 1}° aposta - Digite um número entre 1 e 60: ')))
        l2.sort()

        l3 = []

        for i in l1:
            for j in l2:
                if(j == i):
                    l3.append(i)
                    break

        if(len(l3) > 0):
            if(len(l3) == 6):
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print('\033[33mVocê ganho na Loteria!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
            elif(len(l3) == 5):
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print(f'\033[34mVocê acertou os 5 números: {l3}, \nganhou fazendo a Quina!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
            elif(len(l3) == 4):
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print(f'\033[32mVocê acertou os 4 números: {l3}, \nganhou fazendo a Quadra!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
            elif(len(l3) == 3):
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print(f'\033[35mVocê acertou os 3 números, \napenas os {l3}\nNão foi dessa vez!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
            elif(len(l3) == 2):
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print(f'\033[35mVocê acertou os 2 números, \napenas os {l3}\nNão foi dessa vez!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
            elif(len(l3) == 1):
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print(f'\033[35mVocê acertou 1 número, \napenas o {l3}\nNão foi dessa vez!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
                
            else:
                print('\033[1;34m=\033[m' *50)
                sleep(.3)
                print('\033[31mVocê não acertou!\033[m')
                sleep(.3)
                print(f'Você apostou os números: \033[32m{l2}\033[m')
                sleep(.3)
                print(f'Os números sorteados foram: \033[31m{l1}\033[m')
        else:
            print('\033[1;34m=\033[m' *50)
            sleep(.3)
            print('\033[31mVocê não acertou!\033[m')
            sleep(.3)
            print(f'Você apostou os números: \033[32m{l2}\033[m')
            sleep(.3)
            print(f'Os números sorteados foram: \033[31m{l1}\033[m')

    elif resp !='S' and resp !='N':
        print('\033[31mEscolha errada!\033[m\nEscolha \033[34mSim\033[m ou \033[31mNão\033[m')

    else:
        break
