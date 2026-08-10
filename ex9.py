def maior_menor(a,b):
    if a == b:
        print(f'{a} e {b} são iguais')     
    elif a > b:
        print(f'{a} é maior que {b}')
    else:
        print(f'{a} é menor que {b}')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if __name__ == "__main__":
    maior_menor(numero1,numero2)
