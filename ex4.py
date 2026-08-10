#Usuário digita sua nota
nota = float(input('Digite sua nota: '))

#Função que determina se ele foi aprovado ou não. Acima de 7 pontos*
def nota_final(nota):
    if nota >= 7:
        print('Você foi aprovado!')
    else:
        print('Infelizmente você não alcançou a média, está reprovado.')
    return nota

nota_final(nota)
