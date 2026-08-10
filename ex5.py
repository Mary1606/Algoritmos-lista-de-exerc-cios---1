#Usuário pede um número para mostrar a tabuada
numero = int(input('Digite um número: '))

#Mensagem na tela sobre a tabuada
print(f'\nAqui está a tabuada do número {numero}:')

#Multiplicação e o resultado na tela
for i in range(1,11):
    multiplica = (numero * i)
    print(f'{numero} x {i} = {multiplica}')
