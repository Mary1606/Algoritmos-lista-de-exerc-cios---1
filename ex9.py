#Função para determinar o maior ou o menor número
def maior_menor(a,b):
    if a == b:
        print(f'{a} e {b} são iguais')     
    elif a > b:
        print(f'{a} é maior que {b}')
    else:
        print(f'{a} é menor que {b}')

#Imprimir na tela os números determinados pelo usuário
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

