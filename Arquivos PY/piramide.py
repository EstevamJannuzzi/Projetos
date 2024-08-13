def imagem(pir):

    print('\033[1;32m-\033[m' * 70)
    pir = int(input('\033[1;33mDigite quantas linhas para criar a parte superior da imagem:\033[m '))
    print('\033[1;32m-\033[m' * 70)

    for l in range(pir + 1):
        x = '* '
        x *= l
        print(f'\033[1;31m{x: ^70}\033[m')

    for l in range(pir):
        x = '* '
        x *= pir - l - 1
        print(f'\033[1;34m{x: ^70}\033[m')



while True:
    print('\033[1;32m-\033[m' * 70)
    resp = str(input('\033[1;35mVamos começar a jogar?:\033[m ')).upper()[0]

    if resp =='S':
        imagem(resp)

    elif resp !='S' and resp != 'N':
        print('Responda apenas \033[1;36mSim\033[m ou \033[1;31mNão\033[m!')

    else:
        break
