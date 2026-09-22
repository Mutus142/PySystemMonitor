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
==================================================
                 PY SYSTEM MONITOR
                   ANÁLISE RAM
==================================================

[ MEMÓRIA RAM ]

RAM total:              {ram_total:.2f} GiB
RAM utilizada:          {ram_usada:.2f} GiB
RAM disponível:         {ram_disponivel:.2f} GiB
Uso da RAM:             {ram_percent}%

==================================================
''')

        time.sleep(7)
        print('\nCarregando mais opções...\n')

        while True:

            print('''
==================================================
                O QUE DESEJA FAZER?
==================================================

[1] Voltar ao menu principal
[2] Fazer nova análise da RAM
[3] Sair do programa

==================================================
''')

            try:
                escolha = int(input('Escolha uma opção: '))

            except ValueError:
                print('\n[!] Digite apenas números!\n')
                continue

            if escolha == 1:
                return

            elif escolha == 2:
                print('\nRealizando nova análise da RAM...\n')
                break

            elif escolha == 3:
                print('\nEncerrando PySystemMonitor. Até logo!\n')
                raise SystemExit(0)

            else:
                print('\n[!] Opção inválida! Tente novamente.\n')