soma = 0
#Usuário escolhe um número e só para quando digitar: 0
while True:
    numeros = int(input('Digite um número ou digite 0 para parar: '))
    soma += numeros
    if numeros != 0:
        continue
    else:
        break

#Imprimir na tela o resultado
print(f'\nA soma dos números é igual a: {soma}')
