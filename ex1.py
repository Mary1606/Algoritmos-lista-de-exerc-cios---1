#Números que o usuário irá colocar
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#Funções das 4 operações
def adicao(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    return a / b

#Os resultados de cada cálculo
resultado_adicao = adicao(num1,num2)
resultado_subtracao = subtracao(num1,num2)
resultado_multiplicacao = multiplicacao(num1,num2)
resultado_divisao = round(divisao(num1,num2),2)

#Os valores impressos na tela
print(f'\nAdição: {resultado_adicao} \nSubtração: {resultado_subtracao} \nDivisão: {resultado_divisao} \nMultiplicação: {resultado_multiplicacao}')