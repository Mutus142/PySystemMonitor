import psutil
import time


def dados_disco():

    while True:

        disco = psutil.disk_usage("C:\\")

        disco_total = disco.total / (1024 ** 3)
        disco_usado = disco.used / (1024 ** 3)
        disco_livre = disco.free / (1024 ** 3)
        disco_percent = disco.percent

        print(f'''
========================================
              DADOS DO DISCO
========================================

Espaço total:       {disco_total:.2f} GB
Espaço usado:       {disco_usado:.2f} GB
Espaço livre:       {disco_livre:.2f} GB
Percentual usado:   {disco_percent}%

========================================
''')

        time.sleep(2)
        print('Carregando novas opções...')

        print('''
========================================
           O QUE DESEJA FAZER?
========================================

[1] Voltar ao menu principal
[2] Fazer nova análise do disco
[3] Sair

========================================
''')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            return

        elif escolha == 2:
            print('\nRealizando nova análise do disco...\n')
            continue

        elif escolha == 3:
            print('\nSaindo...')
            break

        else:
            print('\nOpção inválida...\n')