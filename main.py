# MENU INICIAL DE ESCOLHA DE CADA PEÇA/VER MONITOR GERAL 
from Monitor.dadoscpu import dados_cpu
from Monitor.dadosram import dados_ram
from Monitor.dadosdisco import dados_disco
from Monitor.dadosrede import dados_rede
from Monitor.analise import analise


def menu_principal():
    
    while True:

        print('''
        BEM VINDO AO PY SYSTEM MONITOR
        1 - VER ANALISE COMPLETA
        2 - CPU
        3 - RAM
        4 - DISCO
        5 - REDE
    
        ESCOLHA UMA OPÇÃO''')

        escolha = int(input('Qual é sua escolha?: '))

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

        else:
            print('Operação invalida!')
            continue