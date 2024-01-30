from time import sleep


while True:

    print('=' * 100)
    jogar = str(input(f'Vamos jogar? (\033[1;34mSim\033[m ou \033[1;31mNão\033[m): ')).upper()[0]
    
    if jogar == 'S':

        print('=' * 100)
        escolha = int(input('Escolha entre 1 e 3. (Outros valores retorna ao Início): '))

        match escolha:

            case 1:
                sleep(0.5)

                def tabuada(tab):
                    for num in range(1, 11):
                        r = tab * num
                        print(f'\033[1;33m{tab}\033[m x \033[1;36m{num}\033[m = \033[1;31m{r}\033[m')


                while True:
                    
                    print('=' * 100)
                    resp = str(input('Vamos fazer a tabuada? (\033[1;34mSim\033[m ou \033[1;31mNão\033[m): ')).upper()[0]

                    if resp == 'S':
                        tab = int(input('Digite o número para tabuada: ')) 
                        tabuada(tab)

                    elif resp !='S' and resp != 'N':
                        print('Digite apenas \033[1;34mSim\033[m ou \033[1;31mNão\033[m!') 

                    else:
                        break


            case 2:
                sleep(0.5)

                def soma(n1, n2):
                    s = n1 + n2
                    print(f'A soma entre \033[1;33m{n1}\033[m + \033[1;36m{n2}\033[m = \033[1;31m{s}\033[m')

                while True:

                    print('=' * 100)
                    resp = str(input('Vamos somar dois números? (\033[1;34mSim\033[m ou \033[1;31mNão\033[m): ')).upper()[0]

                    if resp == 'S':
                        n1 = int(input('Digite o primeiro número: '))
                        n2 = int(input('Digite o segundo número: '))
                        soma(n1, n2)

                    elif resp !='S' and resp != 'N':
                        print('Digite apenas \033[1;34mSim\033[m ou \033[1;31mNão\033[m!')

                    else:
                        break
                    
                    
            case 3:
                sleep(0.5)

                def conversor(num):
                    print(f'O número \033[1;33m{num}\033[m em Binário é \033[1;36m{bin(num)[2:]}\033[m, \nem Octadecimal é \033[1;31m{oct(num)[2:]}\033[m \ne em hexadecimal é \033[1;35m{hex(num)[2:]}\033[m')
                    
                num = ''

                while True:

                    print('=' * 100)
                    resp = str(input('Vamos converter um número para \033[1;36mBINÁRIO\033[m, \033[1;31mOCTADECIMAL\033[m e \033[1;35mHEXADECIMAL\033[m? (\033[1;34mSim\033[m ou \033[1;31mNão\033[m): ')).upper()[0]

                    if resp == 'S':
                        num = int(input('Digite o número para conversão: '))
                        conversor(num)

                    elif resp !='S' and resp != 'N':
                        print('Digite apenas \033[1;34mSim\033[m ou \033[1;31mNão\033[m!')

                    else:
                        break
                            
        
            case _:
                sleep(1)


    elif jogar != 'S' and jogar != 'N':
        print('Escolha \033[1;34mSim\033[m ou \033[1;31mNão\033[m]!')
    

    else:
        break
                