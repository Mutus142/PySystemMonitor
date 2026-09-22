import psutil
import time

def verificacao_limite():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_percent = ram.percent

    disco = psutil.disk_usage("C:\\")

    disco_percent = disco.percent

    alerta_ativo = False

    if cpu >= 95:
        notificacao_cpu()
        print('Cpu em estado grave!')
        alerta_ativo = True

    if ram_percent >= 90:
        notificacao_ram()
        print('ram em estado grave!')
        alerta_ativo = True

    if disco_percent >= 95:
        notificacao_disco()
        print('disco em estado grave!')
        alerta_ativo = True

    if not alerta_ativo:
        print('Componentes funcionando!')