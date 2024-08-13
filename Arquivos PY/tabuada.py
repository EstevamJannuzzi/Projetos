def tabuada(tab):
    for num in range(1, 11):
        r = tab * num
        print(f'{tab} x {num} = {r}')


while True:
    resp = str(input('Vamos fazer a tabuada? (Sim ou Não): ')).upper()[0]
    if resp == 'S':
        tab = int(input('Digite o número para tabuada: ')) 
        tabuada(tab)
    elif resp !='S' and resp != 'N':
        print('Digite apenas Sim ou Não!')    
    else:
        break
        