numeros = []

for i in range(1,11):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)

soma = sum(numeros)
media = round((soma / 10),2)

print(f'\nA soma dos números digitados é: {soma} \nA média deles é: {media}')
