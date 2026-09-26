
def obter_limites(limites):

    alterar = input('Você deseja alterar algum limite? S/N ').upper()

    if alterar == 'S':

        print('''Selecione a opção para qual peça deseja alterar:
        1 - CPU
        2 - RAM
        3 - DISCO
        ''')

        escolha = int(input('Qual é sua escolha? '))

        if escolha == 1:
            limite_antigo = limites['CPU']
            print('Limite atual da CPU: ', limite_antigo)

            limite_novo = int(input('Qual é o limite novo da CPU? '))

            if 1 <= limite_novo <= 100:
                limites['CPU'] = limite_novo
            else:
                print('Limite inválido!')

        elif escolha == 2:
            limite_antigoram = limites['RAM']
            print('O limite atual da RAM: ', limite_antigoram)

            limite_novoram = int(input('Qual é o novo limite da RAM? '))

            if 1 <= limite_novoram <= 100:
                limites['RAM'] = limite_novoram
            else:
                print('Limite inválido!')

        elif escolha == 3:
            limite_antigodisco = limites['DISCO']
            print('Limite antigo do disco: ', limite_antigodisco)

            limite_novodisco = int(input('Qual é o limite novo do disco? '))
            if 1 <= limite_novodisco <= 100:
                limites['DISCO'] = limite_novodisco
            else:
                print('Limite inválido!')

        else:
            print('Operação cancelada!')

    return limites

if __name__ == "__main__":
    limites = {
        "CPU": 95,
        "RAM": 90,
        "DISCO": 95
    }

    while True:
        configuracoes = obter_limites(limites)
        print(configuracoes)

        continuar = input("Deseja continuar? S/N: ").upper()

        if continuar == "N":
            print("Encerrando configurações...")
            break