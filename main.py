# PY SYSTEM MONITOR V1.1
# MENU PRINCIPAL

from Monitor.dadoscpu import dados_cpu
from Monitor.dadosram import dados_ram
from Monitor.dadosdisco import dados_disco
from Monitor.dadosrede import dados_rede
from Monitor.analise import analise
from Monitor.processos import process
from Monitor.sistema import info_sistema


def sobre():
    print('''
╔══════════════════════════════════════════════════╗
║              SOBRE O PYSYSTEMMONITOR             ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  Projeto:        PySystemMonitor                 ║
║  Versão:         1.1                             ║
║  Desenvolvedor:  Mateus                          ║
║                                                  ║
║  Bibliotecas utilizadas:                         ║
║  • psutil                                        ║
║  • winotify                                      ║
║  • time                                          ║
║  • datetime                                      ║
║                                                  ║
║  Monitoramento de recursos do sistema através    ║
║  do terminal, com análise de CPU, RAM, disco     ║
║  e rede.                                         ║
║                                                  ║
╚══════════════════════════════════════════════════╝
''')

    input('Pressione ENTER para voltar ao menu...')


def menu_principal():

    while True:

        print('''
╔══════════════════════════════════════════════════╗
║                 PY SYSTEM MONITOR                ║
║                      v1.1                        ║
╠══════════════════════════════════════════════════╣
║                  MENU PRINCIPAL                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  [1] Análise completa do sistema                 ║
║  [2] Monitoramento da CPU                        ║
║  [3] Monitoramento da RAM                        ║
║  [4] Monitoramento do disco                      ║
║  [5] Monitoramento da rede
║  [6] Processos em execução
║  [7] Informações do Sistema
   [8] Sobre                                       ║
║                                                  ║
║  [0] Sair do programa                            ║
║                                                  ║
╚══════════════════════════════════════════════════╝
''')

        try:
            escolha = int(input('>> Escolha uma opção: '))

        except ValueError:
            print('''
╔══════════════════════════════════════════════════╗
║ [!] ERRO: Digite apenas números.                 ║
╚══════════════════════════════════════════════════╝
''')
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


        elif escolha == 6:
            process()

        elif escolha == 7:
            info_sistema()

        elif escolha == 8:
            sobre()

        elif escolha == 0:
            print('''
╔══════════════════════════════════════════════════╗
║                                                  ║
║           PySystemMonitor encerrado.             ║
║                   Até logo!                      ║
║                                                  ║
╚══════════════════════════════════════════════════╝
''')
            break

        else:
            print('''
╔══════════════════════════════════════════════════╗
║ [!] Opção inválida. Tente novamente.             ║
╚══════════════════════════════════════════════════╝
''')


if __name__ == "__main__":
    menu_principal()