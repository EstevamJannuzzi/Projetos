from biblioteca import *
from time import sleep


while True:

    print('\033[1;32m=\033[m' * 60)
    print('\033[1;31mCONVERTER VALORES\033[m'.center(70))
    print('\033[1;32m=\033[m' * 60)
    resp = str(input('Vamos calcular um valor? (Sim ou Não) ')).capitalize()[0]
    sleep(.3)

    if resp == 'S':
        programa(resp)

    elif resp != 'S' and resp != 'N':
        print('Responda apenas \033[1;34mSim\033[m ou \033[1;31mNão\033[m!')

    else:
        break
