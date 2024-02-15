import random
def criptografador():
    def cript_palavra(palavra, padrao):
        # Cria uma lista de índices para os caracteres da palavra
        indices = list(range(len(palavra)))

        if padrao == 'inverter':
            indices.reverse()

        elif padrao == 'aleatorio':
            random.shuffle(indices)

        cript_ok = ''.join(palavra[i] for i in indices)
        return cript_ok

    def input_x():
        user_message = input('Digite a mensagem: ')




criptografador()