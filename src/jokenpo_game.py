import random

def ganhar():
    print(f'Ganhou!Você escolheu {py} e eu {com}')
def perder():
    print(f'Perdeu!Você escolheu {py} e eu {com}')
def empate():
    print(f'Empate! Os dois escolheram {com}')


loop = True
lista = ['pedra', 'papel', 'tesoura']
py = 0
count_vitorias = 0
count_derrotas = 0
count_empates = 0
print('\033[33m=-=\033[m' * 20)
print('\033 JOKENPÔ GAME\033[m')
print('\033[33m=-=\033[m' * 20)
while loop:
    print('''[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura''')
    py = int(input('>>> Escolha: '))
    print('\033[33m=-=\033[m' * 20)
    com = random.choice(lista).lower()
    if py == 1:
        py = 'pedra'
        if com == 'tesoura':
            ganhar()
            count_vitorias += 1
        elif com == 'papel':
            perder()
            count_derrotas += 1
        elif com == py:
            empate()
            count_empates += 1
    elif py == 2:
        py = 'papel'
        if com == 'pedra':
            ganhar()
            count_vitorias += 1
        elif com == 'tesoura':
            perder()
            count_derrotas += 1
        elif com == py:
            empate()
            count_empates += 1
    elif py == 3:
        py = 'tesoura'
        if com == 'papel':
            ganhar()
            count_vitorias += 1
        elif com == 'pedra':
            perder()
            count_derrotas += 1
        elif com == py:
            empate()
            count_empates += 1
    else:
        print('Erro, tente novamente!')
    loop = input('Jogar novamente? [S/N] ').strip().lower()
    print('\033[33m=-=\033[m' * 20)
    if loop == 'n':
            loop = False
print('SUA PONTUAÇÃO FINAL')
print('\033[33m=-=\033[m'*20)
print(f'Vitórias: {count_vitorias}')
print(f'Derrotas: {count_derrotas}')
print(f'Empates: {count_empates}')
