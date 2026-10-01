import psutil
import time


def process():

    while True:

        print("\n" + "═" * 70)
        print("                       PROCESSOS EM EXECUÇÃO")
        print("═" * 70)
        print(f"{'PID':<10} │ {'PROCESSO':<35} │ {'RAM':>15}")
        print("─" * 70)

        for processo in psutil.process_iter(["name", "pid", "memory_info"]):

            pid = processo.info["pid"]
            nome = processo.info["name"]
            memory = processo.info["memory_info"].rss / (1024 ** 2)

            print(
                f"{pid:<10} │ "
                f"{nome:<35} │ "
                f"{memory:>10.2f} MB"
            )

        print("═" * 70)
        time.sleep(6)

        print("""
┌─────────────────────────────────────────────┐
│              O QUE DESEJA FAZER?            │
├─────────────────────────────────────────────┤
│  [1] Nova análise                           │
│  [2] Voltar ao menu                         │
└─────────────────────────────────────────────┘
""")

        try:
            escolha = int(input("Escolha uma opção: "))

        except ValueError:
            print("\n[!] Digite apenas um número válido.")
            continue

        if escolha == 1:
            print("\nAtualizando processos...")
            continue

        elif escolha == 2:
            print("\nVoltando ao menu...")
            return

        else:
            print("\n[!] Opção inválida.")