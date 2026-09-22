# PARTE DE DADOS DA RAM

import psutil
import time


def dados_ram():

    while True:

        ram = psutil.virtual_memory()

        ram_total = ram.total / (1024 ** 3)
        ram_usada = ram.used / (1024 ** 3)
        ram_disponivel = ram.available / (1024 ** 3)
        ram_percent = ram.percent

        print(f'''
========================================
             MEMÓRIA RAM
========================================

RAM total:        {ram_total:.2f} GB
RAM usada:        {ram_usada:.2f} GB
RAM disponível:   {ram_disponivel:.2f} GB
Uso da RAM:       {ram_percent}%

========================================
''')

        time.sleep(7)
        print('Carregando mais opções...')

        print('''
========================================
           O QUE DESEJA FAZER?
========================================

[1] Voltar ao menu principal
[2] Fazer nova análise da RAM
[3] Sair

========================================
''')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            return

        elif escolha == 2:
            print('\nRealizando nova análise da RAM...\n')
            continue

        elif escolha == 3:
            print('\nSaindo do sistema...')
            break

        else:
            print('\nOpção inválida...\n')