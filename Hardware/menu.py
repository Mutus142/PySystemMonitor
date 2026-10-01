from Hardware.analisar_hardware import analisar_hardware
from Hardware.analisar_melhorias import sug_melhorias

def analisar_hard():

    while True:

        print("\n" + "═" * 60)
        print("                  ANÁLISE DE HARDWARE")
        print("═" * 60)

        print("""
┌─────────────────────────────────────────────┐
│              O QUE DESEJA FAZER?            │
├─────────────────────────────────────────────┤
│  [1] Analisar peças de hardware             │
│  [2] Sugestões de melhorias                 │
│  [3] Voltar ao menu principal               │
└─────────────────────────────────────────────┘
""")

        try:
            escolha = int(input("Escolha uma opção: "))

        except ValueError:
            print("\n[!] Digite apenas um número válido.")
            continue

        if escolha == 1:
            print("\nAnalisando hardware...")
            analisar_hardware()

        elif escolha == 2:
            print("\nCarregando sugestões...")
            sug_melhorias()

        elif escolha == 3:
            print("\nVoltando ao menu principal...")
            return

        else:
            print("\n[!] Opção inválida.")