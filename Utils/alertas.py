import psutil
import time
from winotify import Notification

alertas_enviados = {
    "CPU": False,
    "RAM": False,
    "DISCO": False
}

def verificacao_limite():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_percent = ram.percent

    disco = psutil.disk_usage("C:\\")

    disco_percent = disco.percent

    alerta_ativo = False

    if cpu >= 95:
        alerta_ativo = True 

        if not alertas_enviados["CPU"]:
            enviar_notificacao("CPU", cpu)
            alertas_enviados["CPU"] = True
            print("CPU em estado grave!")

    else:
        alertas_enviados["CPU"] = False

    if ram_percent >= 90:
        alerta_ativo = True

        if not alertas_enviados["RAM"]:
            enviar_notificacao("RAM", ram_percent)
            alertas_enviados["RAM"] = True
            print("RAM em estado grave!")

    else:
        alertas_enviados["RAM"] = False

    if disco_percent >= 95:
        alerta_ativo = True

        if not alertas_enviados["DISCO"]:
            enviar_notificacao("DISCO", disco_percent)
            alertas_enviados["DISCO"] = True
            print("Disco em estado grave!")

    else:
        alertas_enviados["DISCO"] = False

    if not alerta_ativo:
        print('Componentes funcionando!')


def enviar_notificacao(recurso, porcentagem):
    
    alerta = Notification(
        app_id="PySystemMonitor",
        title=f"Uso elevado da {recurso}!",
        msg=f"{recurso} atingiu {porcentagem}%.",
        duration="short"
    )

    alerta.show()

alertas_enviados["CPU"] = False
print('Pode receber notificação nova')