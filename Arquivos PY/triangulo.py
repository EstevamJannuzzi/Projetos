from math import sqrt

def triangulo (tri):
    if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
            print('Os segmentos \"\033[1;36mFORMAM UM TRIÂNGULO\033[m".')

            if ladoa == ladob == ladoc:
                print('Com todos os segmentos iguais esse triângulo é \033[1;34mEquilátero\033[m.')
                a = ladoa * ladoa * 1.7 / 4
                print(f'E sua área é de \033[1;34m{a:.2f}cm²\033[m.')

            elif ladoa != ladob != ladoc != ladoa:
                print('Com todos os segmentos diferentes uns dos outros esse \ntriângulo é \033[1;31mEscaleno\033[m.')
                p = (ladoa + ladob + ladoc) / 2
                a = sqrt(p * (p - ladoa) * (p - ladob) * (p - ladoc))
                print(f'E sua área é de \033[1;31m{a:.2f}cm²\033[m.')

            else:
                print('Com dois segmentos iguais esse triângulo é \033[1;33mIsósceles\033[m.')
                if ladoa == ladob != ladoc != ladoa:
                     h = sqrt((ladoa * ladoa) - (ladoc * ladoc))
                     a = ((ladoc * 2) * h) / 2
                     print(f'E sua área é de \033[1;33m{a:.2f}cm²\033[m.')
                
                elif ladoa == ladoc != ladob != ladoa:
                     h = sqrt((ladoa * ladoa) - (ladob * ladob))
                     a = ((ladob * 2) * h) / 2
                     print(f'E sua área é de \033[1;33m{a:.2f}cm²\033[m.')

                elif ladoa != ladob == ladoc != ladoa:
                     h = sqrt((ladob * ladob) - (ladoa * ladoa))
                     a = ((ladoa * 2) * h) / 2
                     print(f'E sua área é de \033[1;33m{a:.2f}cm²\033[m.')

    else: 
            print('Os segmentos \"\033[1;31mNÃO FORMAM UM TRIÂNGULO\033[m".')


while True:
    
    print('=' * 60)
    print('\033[1;35mTriângulos\033[m'.center(70))
    print('=' * 60)

    pergunta = str(input('Vamos ver qual triângulo formamos? (Sim ou Não): ')).upper()[0]

    if pergunta == 'S':
        ladoa = float(input('Digite o lado A: '))
        ladob = float(input('Digite o lado B: '))
        ladoc = float(input('Digite o lado C: '))
        print('=' * 60)
        triangulo(pergunta)
 
    elif pergunta != 'S' and pergunta != 'N':
        print('\033[1;34mResponda apenas Sim ou Não!\033[m')

    else:
        break
    