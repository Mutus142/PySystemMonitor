import psutil
import subprocess


def analisar_hardware():

    def obter_cpu():

        comando = [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name"
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        nome = resultado.stdout.strip()

        nucleos = psutil.cpu_count(logical=False)
        threads = psutil.cpu_count(logical=True)
        frequencia = psutil.cpu_freq()

        dados_cpu = {
            "nome": nome,
            "nucleos": nucleos,
            "threads": threads,
            "frequencia_max": frequencia.max
        }

        return dados_cpu

    cpu = obter_cpu()
    print(cpu)