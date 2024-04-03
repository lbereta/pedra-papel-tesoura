from random import choice

movimentos = ['pedra', 'papel', 'tesoura']
ponto_Brenda = 0
ponto_Lucas = 0

for i in range(5):
    movimento_Lucas = choice(movimentos)
    movimento_Brenda = choice(movimentos)

    print(f'Brenda escolheu {movimento_Brenda}')
    print(f'Lucas escolheu {movimento_Lucas}')
    if movimento_Lucas == movimento_Brenda:
        print('Empate')
    elif movimento_Lucas == 'pedra' and movimento_Brenda == 'tesoura':
        print('Ponto para Lucas')
        ponto_Lucas += 1
    elif movimento_Lucas == 'tesoura' and movimento_Brenda == 'papel':
        print('Ponto para Lucas')
        ponto_Lucas += 1
    elif movimento_Lucas == 'papel' and movimento_Brenda == 'pedra':
        print('Ponto para Lucas')
        ponto_Lucas += 1
    else:
        print('Ponto para Brenda')
        ponto_Brenda += 1
    print('\n')

print('\nPontuacao Final')
print(f'Brenda fez {ponto_Brenda} e Lucas fez {ponto_Lucas}!')
if ponto_Lucas > ponto_Brenda:
    print('\nLucas é o vencedor!')
elif ponto_Lucas < ponto_Brenda:
    print('\nBrenda é a vencedora!')
else:
    print('\nDeu empate!')
