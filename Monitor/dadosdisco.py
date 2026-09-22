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
==================================================
                 PY SYSTEM MONITOR
                  ANÁLISE DISCO
==================================================

[ DISCO C: ]

Espaço total:           {disco_total:.2f} GiB
Espaço utilizado:       {disco_usado:.2f} GiB
Espaço livre:           {disco_livre:.2f} GiB
Uso do disco:           {disco_percent}%

==================================================
''')

        time.sleep(7)
        print('\nCarregando novas opções...\n')

        # MENU DE OPÇÕES
        while True:

            print('''
==================================================
                O QUE DESEJA FAZER?
==================================================

[1] Voltar ao menu principal
[2] Fazer nova análise do disco
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
                print('\nRealizando nova análise do disco...\n')
                break

            elif escolha == 3:
                print('\nEncerrando PySystemMonitor. Até logo!\n')
                raise SystemExit(0)

            else:
                print('\n[!] Opção inválida! Tente novamente.\n')