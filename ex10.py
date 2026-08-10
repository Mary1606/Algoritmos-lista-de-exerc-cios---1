numeros = []

for i in range(1,6):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f'Maior número é {maior} \nMenor número é {menor}')
