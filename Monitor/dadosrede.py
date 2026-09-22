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
========================================
              DADOS DA REDE
========================================

Dados recebidos:                {rede_bytesrecebidos:.2f} GB
Dados enviados:                 {rede_bytesenviados:.2f} GB

Pacotes recebidos:              {rede_pacotesrecebidos}
Pacotes enviados:               {rede_pacotesenviados}

Erros de recebimento:           {rede_errosrecebidos}
Erros de envio:                 {rede_errosenviados}

Pacotes recebidos descartados:  {rede_pacotdescart}
Pacotes enviados descartados:   {rede_pacotenvdescart}

========================================
''')

        time.sleep(7)
        print('Carregando mais opções...')

        print('''
========================================
           O QUE DESEJA FAZER?
========================================

[1] Voltar ao menu principal
[2] Fazer nova análise da rede
[3] Sair

========================================
''')

        try:
            escolha = int(input('Escolha uma opção: '))

        except ValueError:
            print('Digite apenas números!')
            continue


        if escolha == 1:
            return

        elif escolha == 2:
            print('\nRealizando nova análise da rede...\n')
            continue

        elif escolha == 3:
            print('\nSaindo...')
            raise SystemExit(0)

        else:
            print('\nOpção inválida!\n')