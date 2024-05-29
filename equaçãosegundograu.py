from math import sqrt

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None  # Não há raízes reais
    elif delta == 0:
        x = -b / (2*a)
        return x  # Uma raiz real
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return x1, x2  # Duas raízes reais

# Exemplo de uso
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

raizes = calcular_raizes(a, b, c)
if raizes:
    print(f"Raízes: {raizes}")
else:
    print("Não há raízes reais.")
