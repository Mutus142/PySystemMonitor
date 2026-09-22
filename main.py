# PY SYSTEM MONITOR V1.1
# MENU PRINCIPAL

from Monitor.dadoscpu import dados_cpu
from Monitor.dadosram import dados_ram
from Monitor.dadosdisco import dados_disco
from Monitor.dadosrede import dados_rede
from Monitor.analise import analise


def menu_principal():

    while True:

        print('''
==================================================
                 PY SYSTEM MONITOR
                     V1.1
==================================================

                  MENU PRINCIPAL

[1] Análise completa do sistema
[2] Monitoramento da CPU
[3] Monitoramento da RAM
[4] Monitoramento do disco
[5] Monitoramento da rede
[0] Sair do programa

==================================================
''')

        try:
            escolha = int(input('Escolha uma opção: '))

        except ValueError:
            print('\n[!] Digite apenas números!\n')
            continue

        if escolha == 1:
            analise()

        elif escolha == 2:
            dados_cpu()

        elif escolha == 3:
            dados_ram()

        elif escolha == 4:
            dados_disco()

        elif escolha == 5:
            dados_rede()

        elif escolha == 0:
            print('\nEncerrando PySystemMonitor. Até logo!\n')
            break

        else:
            print('\n[!] Opção inválida! Tente novamente.\n')


if __name__ == "__main__":
    menu_principal()