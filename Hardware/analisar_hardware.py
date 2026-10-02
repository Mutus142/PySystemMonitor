import psutil
import subprocess
import json

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

        return {
            "nome": resultado.stdout.strip(),
            "nucleos": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True)
        }


    def dados_ram():
        comando = [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer, Capacity, Speed, ConfiguredClockSpeed, SMBIOSMemoryType, PartNumber | ConvertTo-Json"
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        dados = json.loads(resultado.stdout)

        capacidade_gb = round(
            int(dados["Capacity"]) / (1024 ** 3)
        )

        tipos_ram = {
            26: "DDR4",
            34: "DDR5"
        }

        return {
            "fabricante": dados["Manufacturer"].strip(),
            "capacidade": capacidade_gb,
            "tipo": tipos_ram.get(
                dados["SMBIOSMemoryType"],
                "Desconhecido"
            ),
            "frequencia": dados["ConfiguredClockSpeed"],
            "frequencia_max": dados["Speed"],
            "part_number": dados["PartNumber"].strip()
        }


    def dados_gpu():
        comando = [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion | ConvertTo-Json"
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        dados = json.loads(resultado.stdout)

        # Pode haver mais de uma GPU
        if isinstance(dados, dict):
            dados = [dados]

        gpus = []

        for gpu in dados:

            memoria = gpu["AdapterRAM"]

            if memoria:
                memoria_gb = round(
                    int(memoria) / (1024 ** 3),
                    2
                )
            else:
                memoria_gb = "Desconhecido"

            gpus.append({
                "nome": gpu["Name"],
                "memoria_gb": memoria_gb,
                "driver": gpu["DriverVersion"]
            })

        return gpus


    def dados_ssd():
        comando = [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_DiskDrive | Select-Object Model, Manufacturer, Size, MediaType, InterfaceType | ConvertTo-Json"
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        dados = json.loads(resultado.stdout)

        if isinstance(dados, dict):
            dados = [dados]

        discos = []

        for disco in dados:

            tamanho_gb = round(
                int(disco["Size"]) / (1024 ** 3)
            )

            discos.append({
                "modelo": disco["Model"],
                "fabricante": disco["Manufacturer"],
                "capacidade": tamanho_gb,
                "tipo": disco["MediaType"],
                "interface": disco["InterfaceType"]
            })

        return discos


    def dados_placa_mae():
        comando = [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber | ConvertTo-Json"
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        dados = json.loads(resultado.stdout)

        return {
            "fabricante": dados["Manufacturer"],
            "modelo": dados["Product"],
            "serial": dados["SerialNumber"]
        }


    cpu = obter_cpu()
    ram = dados_ram()
    gpu = dados_gpu()
    ssd = dados_ssd()
    placa_mae = dados_placa_mae()

    print("\nCPU:")
    print(cpu)

    print("\nRAM:")
    print(ram)

    print("\nGPU:")
    print(gpu)

    print("\nARMAZENAMENTO:")
    print(ssd)

    print("\nPLACA-MÃE:")
    print(placa_mae)

    hardware = {
    "cpu": cpu,
    "ram": ram,
    "gpu": gpu,
    "armazenamento": ssd,
    "placa_mae": placa_mae
    }

    return hardware