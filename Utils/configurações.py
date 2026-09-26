
def obter_limites():

    limites = {
        "CPU": 95,
        "RAM": 90,
        "DISCO": 95
    }

    alterar = input('Você deseja alterar algum limite? S/N ').upper()

    if alterar == 'S':

        print('''Selecione a opção para qual peça deseja alterar:
        1 - CPU
        2 - RAM
        3 - DISCO
        ''')  

        escolha = int(input('Qual é sua escolha?'))

        if escolha == 1:
            limite_antigo = limites['CPU']
            print('Limite atual da CPU: ', limite_antigo)
            
            limite_novo = int(input('Qual é o limite novo da CPU?'))

            limites['CPU'] = limite_novo