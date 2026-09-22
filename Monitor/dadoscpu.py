
import psutil
import time


def dados_cpu():

    while True:

        cpu_porcent = psutil.cpu_percent(interval=5)
        cpu_nucleos = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()
        cpu_times = psutil.cpu_times()

        print(f'''
==================================================
                 PY SYSTEM MONITOR
                   ANÁLISE CPU
==================================================

[ PROCESSADOR ]

Uso da CPU:             {cpu_porcent}%
Núcleos físicos:        {cpu_nucleos}
Threads:                {cpu_threads}
Frequência atual:       {cpu_freq.current / 1000:.2f} GHz

--------------------------------------------------

[ TEMPOS DA CPU ]

Tempo de usuário:       {cpu_times.user:.2f} s
Tempo do sistema:       {cpu_times.system:.2f} s
Tempo ocioso:           {cpu_times.idle:.2f} s

==================================================
''')

        time.sleep(7)
        while True:

            print('''
==================================================
                O QUE DESEJA FAZER?
==================================================

[1] Voltar ao menu principal
[2] Fazer nova análise da CPU
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
                print('\nRealizando nova análise da CPU...\n')
                break

            elif escolha == 3:
                print('\nEncerrando PySystemMonitor. Até logo!\n')
                raise SystemExit(0)

            else:
                print('\n[!] Opção inválida! Tente novamente.\n')