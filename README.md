
<div align="center">

# 🖥️ PySystemMonitor

### Monitoramento de hardware e recursos do sistema com Python

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.1-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-22C55E?style=for-the-badge)

**Uma ferramenta CLI para acompanhar CPU, memória RAM, disco e rede diretamente pelo terminal.**

[Funcionalidades](#-funcionalidades) •
[Tecnologias](#-tecnologias-utilizadas) •
[Instalação](#-instalação) •
[Próximas versões](#-próximas-funcionalidades)

</div>

---

## 📌 Sobre o projeto

O **PySystemMonitor** é uma aplicação de linha de comando (CLI), desenvolvida em Python, que permite acompanhar os principais recursos de um computador.

O sistema oferece análises individuais da CPU, memória RAM, disco e rede, além de uma análise geral que reúne as informações mais importantes em um único painel.

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

### ⚙️ Recursos adicionais

- Menu principal interativo.
- Análises individuais e análise geral.
- Possibilidade de atualizar os dados.
- Tratamento de entradas inválidas com `try/except`.
- Navegação independente em cada módulo.
- Exibição organizada e padronizada no terminal.

---

## 🛠️ Tecnologias utilizadas

<div align="center">

| Tecnologia | Utilização |
|:---:|:---|
| **Python** | Linguagem principal do projeto |
| **psutil** | Coleta de informações de hardware e do sistema |
| **time** | Controle dos intervalos entre análises |
| **Git** | Versionamento do código-fonte |
| **GitHub** | Hospedagem e documentação do projeto |
| **VS Code** | Ambiente de desenvolvimento |

</div>

### 🐍 Python e psutil

O Python é responsável pela lógica da aplicação, pelos menus interativos e pela organização dos módulos.

A biblioteca `psutil` permite acessar informações como utilização da CPU, consumo de memória, armazenamento e estatísticas de rede.

O módulo nativo `time` controla os intervalos de espera definidos para cada análise.

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
└── Monitor/
    ├── analise.py
    ├── dadoscpu.py
    ├── dadosram.py
    ├── dadosdisco.py
    └── dadosrede.py
```

O arquivo `main.py` controla o menu principal e a navegação.

Os arquivos da pasta `Monitor/` são responsáveis pela coleta e exibição das informações de cada componente.

---

## 🖥️ Prévia do sistema

Exemplo ilustrativo da análise geral:

```text
==================================================
                 PY SYSTEM MONITOR
                   ANÁLISE GERAL
==================================================

[ CPU ]

Uso da CPU:             15.4%
Núcleos físicos:        8
Threads:                12
Frequência atual:       2.10 GHz

--------------------------------------------------

[ MEMÓRIA RAM ]

Uso da RAM:             58.3%
RAM utilizada:          4.49 GiB
RAM disponível:         3.22 GiB
RAM total:              7.71 GiB

--------------------------------------------------

[ DISCO C: ]

Uso do disco:           64.2%
Espaço utilizado:       305.24 GiB
Espaço livre:           170.18 GiB
Espaço total:           475.42 GiB

--------------------------------------------------

[ REDE ]

Dados recebidos:        1.58 GiB
Dados enviados:         0.24 GiB
Pacotes recebidos:      1225410
Pacotes enviados:       449009

==================================================
```

### 📋 Menu principal

```text
==================================================
                 PY SYSTEM MONITOR
                     V1.1
==================================================

                  MENU PRINCIPAL

[1] Análise completa do sistema
[2] Monitoramento da CPU
[3] Monitoramento da RAM
[4] Monitoramento do disco
[5] Monitoramento da rede
[0] Sair do programa

==================================================
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
> A versão atual foi desenvolvida para Windows. O módulo de disco utiliza a unidade `C:\`, que pode precisar ser alterada em outros sistemas operacionais.

---

## 📝 Histórico de versões

### 🟢 V1.1 — Correções e padronização

- Correção do encerramento do programa.
- Formatação da frequência e dos tempos da CPU.
- Tratamento de entradas inválidas.
- Separação dos loops de análise e navegação.
- Padronização visual de todos os módulos.
- Organização dos arquivos e documentação.

### 🔵 V1.0 — Versão inicial

- Implementação dos módulos de CPU, RAM, disco e rede.
- Criação da análise geral do sistema.
- Desenvolvimento do menu principal interativo.
- Integração entre os módulos.

---

## 🔮 Próximas funcionalidades

Funcionalidades planejadas para futuras versões:

- [ ] Monitoramento contínuo em tempo real.
- [ ] Velocidades de download e upload.
- [ ] Alertas de consumo elevado de CPU, RAM e disco.
- [ ] Interface aprimorada com a biblioteca Rich.
- [ ] Exportação de relatórios.
- [ ] Monitoramento de processos.
- [ ] Informações adicionais das interfaces de rede.

---

## 👨‍💻 Desenvolvedor

<div align="center">

### Mateus — Mutus142

Projeto desenvolvido para aprimorar conhecimentos em Python, monitoramento de sistemas e desenvolvimento de aplicações modulares.

[![GitHub](https://img.shields.io/badge/GitHub-Mutus142-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mutus142)

**⭐ Se gostou do projeto, considere deixar uma estrela no repositório!**

</div>