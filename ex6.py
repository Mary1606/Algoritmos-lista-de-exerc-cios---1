n = int(input('Digite um número: '))

def somatorio(numero):
    soma = 0
    for i in range(1,numero +1):
        soma += i
    return soma

resultado = somatorio(n)
print(f'Seu resultado é {resultado}')