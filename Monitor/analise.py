
import psutil
import time


def analise():

    while True:

        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_nucleos = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()

        disco = psutil.disk_usage("C:\\")

        disco_total = disco.total / (1024 ** 3)
        disco_usado = disco.used / (1024 ** 3)
        disco_livre = disco.free / (1024 ** 3)
        disco_percent = disco.percent

        ram = psutil.virtual_memory()

        ram_total = ram.total / (1024 ** 3)
        ram_usado = ram.used / (1024 ** 3)
        ram_disponivel = ram.available / (1024 ** 3)
        ram_percent = ram.percent

        rede = psutil.net_io_counters()

        rede_bytesrecebidos = rede.bytes_recv / (1024 ** 3)
        rede_bytesenviados = rede.bytes_sent / (1024 ** 3)

        rede_pacotesrecebidos = rede.packets_recv
        rede_pacotesenviados = rede.packets_sent

        print(f'''
==================================================
                 PY SYSTEM MONITOR
                   ANÁLISE GERAL
==================================================

[ CPU ]

Uso da CPU:             {cpu_percent}%
Núcleos físicos:        {cpu_nucleos}
Threads:                {cpu_threads}
Frequência atual:       {cpu_freq.current / 1000:.2f} GHz

--------------------------------------------------

[ MEMÓRIA RAM ]

Uso da RAM:             {ram_percent}%
RAM utilizada:          {ram_usado:.2f} GiB
RAM disponível:         {ram_disponivel:.2f} GiB
RAM total:              {ram_total:.2f} GiB

--------------------------------------------------

[ DISCO C: ]

Uso do disco:           {disco_percent}%
Espaço utilizado:       {disco_usado:.2f} GiB
Espaço livre:           {disco_livre:.2f} GiB
Espaço total:           {disco_total:.2f} GiB

--------------------------------------------------

[ REDE ]

Dados recebidos:        {rede_bytesrecebidos:.2f} GiB
Dados enviados:         {rede_bytesenviados:.2f} GiB
Pacotes recebidos:      {rede_pacotesrecebidos}
Pacotes enviados:       {rede_pacotesenviados}

==================================================
''')

        time.sleep(10)

        while True:

            print('''
==================================================
                O QUE DESEJA FAZER?
==================================================

[1] Voltar ao menu principal
[2] Fazer nova análise geral
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
                print('\nRealizando nova análise geral...\n')
                break

            elif escolha == 3:
                print('\nEncerrando PySystemMonitor. Até logo!\n')
                raise SystemExit(0)

            else:
                print('\n[!] Opção inválida! Tente novamente.\n')