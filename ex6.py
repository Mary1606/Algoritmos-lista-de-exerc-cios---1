#Usuário digita um número
n = int(input('Digite um número: '))

#Função que determina o somatorio dos número 1 até o n
def somatorio(numero):
    soma = 0
    for i in range(1,numero +1):
        soma += i
    return soma

#Imprimir na tela o resultado
resultado = somatorio(n)
print(f'Seu resultado é {resultado}')
