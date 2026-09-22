import psutil
import time
from winotify import Notification

def verificacao_limite():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_percent = ram.percent

    disco = psutil.disk_usage("C:\\")

    disco_percent = disco.percent

    alerta_ativo = False

    if cpu >= 95:
        enviar_notificacao("CPU: ", cpu)
        print('Cpu em estado grave!')
        alerta_ativo = True

    if ram_percent >= 90:
        enviar_notificacao("RAM: ", ram_percent)
        print('ram em estado grave!')
        alerta_ativo = True

    if disco_percent >= 95:
        enviar_notificacao("DISCO: ", disco_percent)
        print('disco em estado grave!')
        alerta_ativo = True

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