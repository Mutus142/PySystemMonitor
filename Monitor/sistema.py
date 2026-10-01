import psutil
import time
import platform
from datetime import datetime


def info_sistema():

    while True:

        sistema = platform.system()
        versao = platform.release()
        arq = platform.machine()
        proces = platform.processor()
        nome = platform.node()

        data = datetime.fromtimestamp(psutil.boot_time())
        data_formatada = data.strftime("%d/%m/%Y - %H:%M:%S")

        agora = datetime.now()
        tempo_ligado = agora - data

        dias = tempo_ligado.days
        segundos = tempo_ligado.seconds

        horas = segundos // 3600
        minutos = (segundos % 3600) // 60

        print("\n" + "═" * 65)
        print("                   INFORMAÇÕES DO SISTEMA")
        print("═" * 65)

        print(f"""
 Sistema Operacional : {sistema}
 Versão              : {versao}
 Arquitetura         : {arq}
 Processador         : {proces}
 Nome do Computador  : {nome}

 Inicializado em     : {data_formatada}
 Tempo Ligado        : {dias}d {horas}h {minutos}min
""")

        time.sleep(7)
        print("""
┌─────────────────────────────────────────────┐
│              O QUE DESEJA FAZER?            │
├─────────────────────────────────────────────┤
│  [1] Nova análise                           │
│  [2] Voltar ao menu principal               │
└─────────────────────────────────────────────┘
""")

        try:
            escolha = int(input("Escolha uma opção: "))

        except ValueError:
            print("\n[!] Insira um número válido!")
            continue

        if escolha == 1:
            print("\nAtualizando informações...")
            continue

        elif escolha == 2:
            print("\nVoltando ao menu principal...")
            return

        else:
            print("\n[!] Opção inválida!")