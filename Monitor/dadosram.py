import psutil
import time
from main import menu_principal

def dados_ram():

    while True:

        ram = psutil.virtual_memory()

        ram_total = ram.total / ( 1024 ** 3 )
        ram_usada = ram.used / ( 1024 ** 3 )
        ram_livre = ram.free / ( 1024 ** 3 )
        ram_percent = ram.percent()

        print(f'''
        OS DADOS DA SUA MEMORIA RAM:
        
        Ram total: {ram_total}GB 
        Ram usada: {ram_usada}GB
        Ram livre: {ram_livre}GB
        Percentual da ram usada: {ram_percent}%
        ''')

        time.sleep(7)
        print('Carregando mais opções...')

        print('''
        O QUE DESEJA FAZER AGORA? 
        
        1 - VOLTAR AO MENU PRINCIPAL
        2 - FAZER NOVA ANALISE NA RAM
        3 - SAIR
        ''')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            menu_principal()

        elif escolha == 2:
            continue

        elif escolha == 3:
            print('Saindo do sistema...')
            break

        else:
            print('Opção invalida...')
            