
import psutil
import time
from winotify import Notification

alertas_enviados = {
    "CPU": False,
    "RAM": False,
    "DISCO": False
}


def enviar_notificacao(recurso, porcentagem):
    try:
        print(f"Tentando enviar notificação: {recurso}")

        alerta = Notification(
            app_id="PySystemMonitor",
            title=f"Alerta de utilização: {recurso}",
            msg=f"{recurso} atingiu {porcentagem:.1f}%.",
            duration="short"
        )

        alerta.show()
        print(f"Notificação solicitada ao Windows: {recurso}")

        return True

    except Exception as erro:
        print(f"Erro ao enviar notificação: {erro}")
        return False


def verificacao_limite():
    cpu = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disco_percent = psutil.disk_usage("C:\\").percent

    componentes = {
        "CPU": (cpu, 95),
        "RAM": (ram_percent, 90),
        "DISCO": (disco_percent, 95)
    }

    alerta_ativo = False

    for recurso, (uso, limite) in componentes.items():

        if uso >= limite:
            alerta_ativo = True

            if not alertas_enviados[recurso]:
                if enviar_notificacao(recurso, uso):
                    alertas_enviados[recurso] = True

                print(f"{recurso} em estado grave!")

        else:
            alertas_enviados[recurso] = False

    if not alerta_ativo:
        print("Componentes dentro dos limites!")


def monitorar_limite():
    print("PySystemMonitor iniciado!")

    try:
        while True:
            verificacao_limite()
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado!")


if __name__ == "__main__":
    monitorar_limite()
