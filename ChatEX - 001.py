import random

def jogo_adivinhacao():
    cpu_esc = random.randint(1,100)
    print('Seja muito bem-vindo ao Jogo de Adivinhação!')
    print('Tente adivinhar um número entre 1 e 100.')

    tentativas = 0

    while True:
        tentativa = int(input('Sua tentativa: '))
        tentativas += 1

        if tentativa == cpu_esc:
            print ('Parabéns! Você acertou o número {} em {} tentativas'.format(cpu_esc, tentativas))
            break
        elif tentativa < cpu_esc:
            print('Muito baixo! Tente novamente.')

        else:
            print('Muito alto! Tente novamente.')


jogo_adivinhacao()