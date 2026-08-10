#Digitar um número 
numero = int(input('Digite um número: '))

#Condição pra ver se ele é positivo ou não
if numero == 0:
    print(f'O número que você digitou é zero')
elif numero > 0:
    print(f'O número {numero} é positivo')
else:
    print(f'O número {numero} é negativo')


