🖥️ PySystemMonitor
🖥️ PySystemMonitor

Monitoramento de hardware e recursos do sistema diretamente pelo terminal, desenvolvido em Python.

📌 Sobre o projeto

O PySystemMonitor é uma aplicação de linha de comando (CLI) desenvolvida em Python para monitorar os principais recursos de um computador.

O projeto permite consultar individualmente o desempenho da CPU, o consumo de memória RAM, a utilização do disco e as estatísticas da rede. Também oferece uma análise geral que reúne as principais informações do sistema em um único painel no terminal.

O objetivo é colocar em prática conceitos de programação Python, modularização, tratamento de erros e coleta de informações do sistema operacional.

🚀 Funcionalidades
Módulo	Funcionalidades
🧠 CPU	Percentual de utilização, núcleos físicos, threads, frequência e tempos de processamento
💾 RAM	Memória total, utilizada, disponível e percentual de uso
💿 Disco	Capacidade total, espaço utilizado, espaço livre e percentual de ocupação
🌐 Rede	Dados recebidos e enviados, pacotes transmitidos, erros e descartes
📊 Análise geral	Visão consolidada dos principais indicadores do computador
⚙️ Recursos adicionais
Menu interativo para navegar entre os módulos.
Possibilidade de atualizar as análises.
Tratamento de entradas inválidas com try/except.
Exibição organizada dos resultados.
Estrutura modular para facilitar a manutenção e a expansão do projeto.
🛠️ Tecnologias utilizadas

Python

Linguagem principal utilizada no desenvolvimento do sistema, responsável pela coleta, processamento e apresentação dos dados.

psutil

Biblioteca que permite acessar informações sobre CPU, memória RAM, disco, rede e outros recursos do sistema operacional.

time

Módulo nativo do Python utilizado para controlar os intervalos entre as análises e a exibição dos menus.

Git e GitHub

Utilizados para versionamento do código-fonte, organização das atualizações e publicação do projeto.

Visual Studio Code

Ambiente de desenvolvimento utilizado para escrever, organizar e executar o código.

📂 Estrutura do projeto
PySystemMonitor/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── Monitor/
    ├── analise.py
    ├── dadoscpu.py
    ├── dadosram.py
    ├── dadosdisco.py
    └── dadosrede.py

Cada módulo é responsável por uma análise específica, enquanto main.py controla o menu principal e a navegação entre as funcionalidades.

🖥️ Prévia do sistema

Exemplo ilustrativo da análise geral apresentada no terminal:

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
📥 Instalação

1. Clone o repositório

git clone https://github.com/Mutus142/PySystemMonitor.git

2. Acesse a pasta do projeto

cd PySystemMonitor

3. Instale as dependências

Certifique-se de ter o Python instalado.

python -m pip install -r requirements.txt

4. Execute o programa

python main.py

O menu principal será exibido no terminal para que você escolha o tipo de análise desejado.

Observação: a versão atual foi desenvolvida para Windows. O monitoramento do disco utiliza a unidade C:\, que pode precisar ser alterada em outros sistemas operacionais.

📝 Histórico de versões
V1.0 — Versão inicial
Implementação dos módulos de CPU, RAM, disco e rede.
Criação da análise geral.
Desenvolvimento do menu principal interativo.
V1.1 — Correções e padronização
Correção do encerramento do programa.
Formatação da frequência e dos tempos da CPU.
Tratamento de entradas inválidas.
Separação entre os loops de análise e de navegação.
Padronização visual dos módulos e menus.
Organização dos arquivos do projeto.
🔮 Próximas funcionalidades

Funcionalidades planejadas para futuras versões:

Monitoramento contínuo em tempo real.
Medição das velocidades de download e upload.
Alertas para consumo elevado de CPU, RAM e disco.
Interface aprimorada com a biblioteca Rich.
Exportação de relatórios.
Informações adicionais sobre processos e interfaces de rede.
👨‍💻 Desenvolvedor

Mateus — Mutus142

Projeto desenvolvido para aprimorar conhecimentos em Python, monitoramento de sistemas e desenvolvimento de aplicações modulares.

⭐ Se você gostou do projeto, deixe uma estrela no repositório!