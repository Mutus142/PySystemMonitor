import psutil
import time

def process():

    while True:

        for processo in psutil.process_iter(["name", "pid", "memory_info"]):
            pid = processo.info["pid"]
            nome = processo.info["name"]
            memory = processo.info["memory_info"].rss / (1024 ** 2)

            print(f'''
            PID: {pid} NOME: {nome} RAM: {memory}''')

        time.sleep(6)
        print('''Deseja fazer nova analise ou voltar para o menu?
        1 - Nova analise
        2 - Voltar
        ''')

        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Escolha um numero válido!')


        if escolha == 1:
            print('Carregando nova analise...')
            continue

        elif escolha == 2:
            print('Voltando...')
            return

        else:
            print('Escolha invalida!')