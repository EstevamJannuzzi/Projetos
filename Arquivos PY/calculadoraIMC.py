while True:

    def imc(nome, altura, peso):

        imc = peso / (altura * altura)
        if imc < 18.5:
            print(f'Senhor(a) {nome}, seu \033[1;32mIMC = {imc:.1f}\033[m e você está\n\033[1;36mclassificado(a) "MAGREZA", obesidade(grau) = 0\033[m')
        elif imc >= 18.5 and imc <= 24.9:
            print(f'Senhor(a) {nome}, seu \033[1;32mIMC = {imc:.1f}\033[m e você está\n\033[1;34mclassificado(a) "NORMAL", obesidade(grau) = 0\033[m')
        elif imc >= 25.0 and imc <= 29.9:
            print(f'Senhor(a) {nome}, seu \033[1;32mIMC = {imc:.1f}\033[m e você está\n\033[1;32mclassificado(a) "SOBREPESO", obesidade(grau) = I\033[m')
        elif imc >= 30.0 and imc <= 39.9:
            print(f'Senhor(a) {nome}, seu \033[1;32mIMC = {imc:.1f}\033[m e você está\n\033[1;35mclassificado(a) "OBESIDADE", obesidade(grau) = II\033[m')
        else:
            print(f'Senhor(a) {nome}, seu \033[1;32mIMC = {imc:.1f}\033[m e você está\n\033[1;31mclassificado(a) "OBESIDADE GRAVE", obesidade(grau) = III\033[m')

    print('=' * 60)
    texto = 'Programa de controle IMC'
    print(f'\033[1;31m{texto}\033[m'.center(70))
    print('=' * 60)

    resp = str(input('Vamos calcular seu IMC? (Sim ou Não): ')).upper()[0]
    if resp == 'S':
        nome = str(input('Digite seu nome: ')).capitalize().strip()
        altura = float(input('Digite sua altura.(Use . ao invés de , para separar números): '))
        peso = float(input('Digite seu peso.(Use . ao invés de , para separar números): '))
        print('=' * 60)
        imc(nome, altura, peso)
        print('=' * 60)
    
    elif resp != 'S' and resp != 'N':
        print('Apenas digite \033[1;33mSim\033[m ou \033[1;31mNão\033[m!')
    
    else:
        break
