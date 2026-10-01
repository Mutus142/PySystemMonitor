<div align="center">

# 🖥️ PySystemMonitor

### Monitoramento de hardware, processos e recursos do sistema com Python

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.2-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-22C55E?style=for-the-badge)

**Uma ferramenta CLI para monitorar CPU, memória RAM, disco, rede, processos e informações do sistema diretamente pelo terminal.**

[Funcionalidades](#-funcionalidades) •
[Tecnologias](#️-tecnologias-utilizadas) •
[Instalação](#-instalação) •
[Próximas versões](#-próximas-funcionalidades)

</div>

---

## 📌 Sobre o projeto

O **PySystemMonitor** é uma aplicação de linha de comando (CLI), desenvolvida em Python, criada para acompanhar diferentes recursos de um computador diretamente pelo terminal.

O sistema permite visualizar informações da CPU, memória RAM, disco e rede, além de realizar uma análise geral, acompanhar processos em execução e consultar informações do sistema operacional.

O projeto foi desenvolvido com o objetivo de aprimorar conhecimentos em **Python, modularização, tratamento de erros, bibliotecas externas e monitoramento de sistemas operacionais**.

---

## 🚀 Funcionalidades

| Módulo | Funcionalidades |
|:---|:---|
| 🧠 **CPU** | Utilização, núcleos físicos, threads, frequência e tempos de processamento |
| 💾 **RAM** | Memória total, utilizada, disponível e percentual de uso |
| 💿 **Disco** | Capacidade total, espaço utilizado, espaço livre e percentual de ocupação |
| 🌐 **Rede** | Dados enviados e recebidos, pacotes, erros e descartes |
| 📊 **Análise geral** | Visão consolidada dos principais indicadores do computador |
| ⚙️ **Processos** | PID, nome do processo e consumo de memória RAM |
| 🖥️ **Sistema** | Sistema operacional, versão, arquitetura, processador, nome do computador e uptime |

### ⚙️ Recursos adicionais

- Menu principal interativo.
- Análises individuais e análise geral.
- Monitoramento dos processos em execução.
- Informações detalhadas do sistema operacional.
- Exibição do tempo de atividade do computador.
- Limites configuráveis para utilização de recursos.
- Alertas de consumo elevado.
- Possibilidade de atualizar as análises.
- Tratamento de entradas inválidas com `try/except`.
- Navegação independente em cada módulo.
- Interface padronizada diretamente no terminal.

---

## 🛠️ Tecnologias utilizadas

<div align="center">

| Tecnologia | Utilização |
|:---:|:---|
| **Python** | Linguagem principal do projeto |
| **psutil** | Coleta de informações do sistema, hardware e processos |
| **platform** | Informações sobre sistema operacional e arquitetura |
| **datetime** | Datas, horários e cálculo do uptime |
| **time** | Controle dos intervalos entre análises |
| **winotify** | Exibição de notificações e alertas no Windows |
| **Git** | Versionamento do código-fonte |
| **GitHub** | Hospedagem e documentação do projeto |
| **VS Code** | Ambiente de desenvolvimento |

</div>

### 🐍 Python e bibliotecas

O Python é responsável pela lógica da aplicação, menus, tratamento de entradas e organização dos módulos.

A biblioteca `psutil` permite acessar informações sobre CPU, memória RAM, armazenamento, rede e processos em execução.

O módulo `platform` fornece informações sobre o sistema operacional, arquitetura e processador.

O módulo `datetime` é utilizado para trabalhar com datas, horários e calcular há quanto tempo o computador está ligado.

O módulo `time` controla os intervalos entre determinadas análises.

A biblioteca `winotify` é utilizada para gerar notificações no Windows quando os limites definidos são atingidos.

---

## 📂 Estrutura do projeto

```text
PySystemMonitor/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── Monitor/
│   ├── analise.py
│   ├── dadoscpu.py
│   ├── dadosram.py
│   ├── dadosdisco.py
│   ├── dadosrede.py
│   ├── processos.py
│   └── sistema.py
│
└── Utils/
    ├── alertas.py
    └── configurações.py
```

O arquivo `main.py` controla o menu principal e a navegação entre os módulos.

A pasta `Monitor/` concentra as funções responsáveis pela coleta e exibição das informações do computador.

A pasta `Utils/` contém recursos auxiliares, como configurações de limites e sistema de alertas.

---

## 🖥️ Prévia do sistema

Exemplo ilustrativo da análise geral:

```text
============================================================
                     PY SYSTEM MONITOR
                       ANÁLISE GERAL
============================================================

[ CPU ]

Uso da CPU:             15.4%
Núcleos físicos:        8
Threads:                 12
Frequência atual:        2.10 GHz

------------------------------------------------------------

[ MEMÓRIA RAM ]

Uso da RAM:             58.3%
RAM utilizada:          4.49 GiB
RAM disponível:         3.22 GiB
RAM total:              7.71 GiB

------------------------------------------------------------

[ DISCO C: ]

Uso do disco:           64.2%
Espaço utilizado:       305.24 GiB
Espaço livre:           170.18 GiB
Espaço total:           475.42 GiB

------------------------------------------------------------

[ REDE ]

Dados recebidos:        1.58 GiB
Dados enviados:         0.24 GiB
Pacotes recebidos:      1225410
Pacotes enviados:       449009

============================================================
```

### 📋 Menu principal

```text
============================================================
                     PY SYSTEM MONITOR
                           V1.2
============================================================

                       MENU PRINCIPAL

[1] Análise completa do sistema
[2] Monitoramento da CPU
[3] Monitoramento da RAM
[4] Monitoramento do disco
[5] Monitoramento da rede
[6] Processos em execução
[7] Informações do sistema
[0] Sair do programa

============================================================
```

### ⚙️ Monitoramento de processos

```text
══════════════════════════════════════════════════════════════════════
                       PROCESSOS EM EXECUÇÃO
══════════════════════════════════════════════════════════════════════
PID        │ PROCESSO                            │             RAM
──────────────────────────────────────────────────────────────────────
19076      │ Code.exe                            │       21.60 MB
12840      │ chrome.exe                          │      315.42 MB
8452       │ python.exe                          │       18.73 MB
══════════════════════════════════════════════════════════════════════
```

### 🖥️ Informações do sistema

```text
═════════════════════════════════════════════════════════════════
                   INFORMAÇÕES DO SISTEMA
═════════════════════════════════════════════════════════════════

 Sistema Operacional : Windows
 Versão              : 11
 Arquitetura         : AMD64
 Processador         : Intel64 Family...
 Nome do Computador  : DESKTOP-XXXXX

 Inicializado em     : 30/09/2026 - 13:26:31
 Tempo Ligado        : 0d 8h 19min

═════════════════════════════════════════════════════════════════
```

---

## 📥 Instalação

### 1. Clone o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Mutus142/PySystemMonitor.git
```

### 2. Acesse a pasta

```bash
cd PySystemMonitor
```

### 3. Instale as dependências

É necessário ter o Python instalado.

```bash
python -m pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python main.py
```

O menu principal será exibido no terminal.

> [!NOTE]
> A versão atual foi desenvolvida para Windows. Algumas funcionalidades, como notificações e monitoramento da unidade `C:\`, são específicas desse sistema operacional.

---

## 📝 Histórico de versões

### 🟣 V1.2 — Processos, sistema e monitoramento

- Implementação do monitoramento de processos.
- Exibição de PID, nome e consumo de RAM dos processos.
- Novo módulo de informações do sistema.
- Identificação do sistema operacional, versão e arquitetura.
- Exibição de informações do processador e nome do computador.
- Exibição da data e hora de inicialização.
- Cálculo do tempo de atividade do sistema.
- Implementação de limites configuráveis.
- Sistema de alertas para consumo elevado.
- Novas melhorias visuais e de navegação.

### 🟢 V1.1 — Correções e padronização

- Correção do encerramento do programa.
- Formatação da frequência e dos tempos da CPU.
- Tratamento de entradas inválidas.
- Separação dos loops de análise e navegação.
- Padronização visual dos módulos.
- Organização dos arquivos e documentação.

### 🔵 V1.0 — Versão inicial

- Implementação dos módulos de CPU, RAM, disco e rede.
- Criação da análise geral do sistema.
- Desenvolvimento do menu principal interativo.
- Integração entre os módulos.

---

## 🔮 Próximas funcionalidades

Ideias planejadas para futuras versões:

- [ ] Histórico das análises.
- [ ] Armazenamento dos dados em JSON ou CSV.
- [ ] Persistência das configurações de limites.
- [ ] Histórico de alertas.
- [ ] Exportação de relatórios.
- [ ] Busca e filtragem de processos.
- [ ] Ranking de processos por consumo de CPU e RAM.
- [ ] Velocidades de download e upload.
- [ ] Interface aprimorada para o terminal.

---

## 👨‍💻 Desenvolvedor

<div align="center">

### Mateus — Mutus142

Projeto desenvolvido para aprimorar conhecimentos em Python, monitoramento de sistemas e desenvolvimento de aplicações modulares.

[![GitHub](https://img.shields.io/badge/GitHub-Mutus142-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mutus142)

**⭐ Se gostou do projeto, considere deixar uma estrela no repositório!**

</div>
