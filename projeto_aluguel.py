import time


print('Aqui está a lista de categorias disponíveis para locação: \n '
'- Hatch \n '
'- Sedan \n '
'- Furgão \n '
'- Mini Van ')
print('')

class Carros:
    categorias_on = ['Hatch', 'Sedan', 'Furgão', 'Mini Van']
    def __init__(self, modelo, cor, ano, categoria):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

escolha = input('Escolha a categoria desejada: ')
escolha = escolha.lower()

for escolha in Carros.categorias_on:

    if escolha == Carros.categorias_on:
        print('')
        print('Processando...')
        time.sleep(1)
        print('Ótima escolha!')
        break
else:
    print('Esta categoria não está disponível no momento. Tente novamente! ')
    input('Escolha a categoria desejada: ')
    print('')
    print('Processando...')
    time.sleep(1)
    print('Ótima escolha!')



