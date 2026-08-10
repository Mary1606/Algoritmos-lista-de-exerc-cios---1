#Lista dos números que o usuário escolheu
numeros = []

#Usuário escolhe os números e são adicionados a lista
for i in range(1,11):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)

#Soma e média dos números da lista
soma = sum(numeros)
media = round((soma / 10),2)

#Imprimir na tela o resultado
print(f'\nA soma dos números digitados é: {soma} \nA média deles é: {media}')
