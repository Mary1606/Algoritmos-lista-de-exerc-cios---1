#Lista de números escolhidos pelo usuário
numeros = []

#Usuário escolhe os números e eles são adicionados a uma lista
for i in range(1,6):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)

#Determinam qual o maior e o menor número dentro da lista
maior = max(numeros)
menor = min(numeros)

#Imprimir na tela o resultado 
print(f'Maior número é {maior} \nMenor número é {menor}')
