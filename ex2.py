#Usuário coloca seu nome e sua idade
nome = (input('Olá! Digite seu nome, por gentileza: '))
idade = int(input('Agora digite sua idade: '))

#Imprimir na tela suas informações
print(f'\nMuito prazer {nome}! Aqui estão as suas informações: \nNome: {nome} \nIdade: {idade}')

#Caso seja usuado futuramente, guardar as informções dele nessa lista
informacoes_usuario = []
informacoes_usuario.append(nome)
informacoes_usuario.append(idade)
