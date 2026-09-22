import psutil
import time

def dados_rede():

    while True:

        rede = psutil.net_io_counters()

        rede_bytesrecebidos = rede.bytes_recv / (1024 ** 3)
        rede_bytesenviados = rede.bytes_sent / (1024 ** 3)

        rede_pacotesrecebidos = rede.packets_recv
        rede_pacotesenviados = rede.packets_sent

        rede_errosrecebidos = rede.errin
        rede_errosenviados = rede.errout

        rede_pacotdescart = rede.dropin
        rede_pacotenvdescart = rede.dropout

        print(f'''
==================================================
                 PY SYSTEM MONITOR
                   ANÁLISE REDE
==================================================

[ TRÁFEGO ACUMULADO ]

Dados recebidos:                 {rede_bytesrecebidos:.2f} GiB
Dados enviados:                  {rede_bytesenviados:.2f} GiB

--------------------------------------------------

[ PACOTES ]

Pacotes recebidos:               {rede_pacotesrecebidos}
Pacotes enviados:                {rede_pacotesenviados}

--------------------------------------------------

[ ERROS E DESCARTES ]

Erros de recebimento:            {rede_errosrecebidos}
Erros de envio:                  {rede_errosenviados}
Pacotes recebidos descartados:   {rede_pacotdescart}
Pacotes enviados descartados:    {rede_pacotenvdescart}

==================================================
''')

        time.sleep(7)
        while True:

            print('''
==================================================
                O QUE DESEJA FAZER?
==================================================

[1] Voltar ao menu principal
[2] Fazer nova análise da rede
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
                print('\nAtualizando dados da rede...\n')
                break

            elif escolha == 3:
                print('\nEncerrando PySystemMonitor. Até logo!\n')
                raise SystemExit(0)

            else:
                print('\n[!] Opção inválida! Tente novamente.\n')