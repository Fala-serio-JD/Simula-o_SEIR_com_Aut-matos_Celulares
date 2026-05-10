# Simulação Epidemiológica SEIRD em Grade Bidimensional

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

## 📋 Descrição do Projeto

Este projeto implementa uma simulação do modelo epidemiológico **SEIRD** (*Suscetível, Exposto, Infectado, Recuperado, Óbito*) utilizando o conceito de **Autômatos Celulares (CA)** em uma grade bidimensional.

Diferente dos modelos matemáticos tradicionais (equações diferenciais) que assumem uma mistura homogênea da população, esta abordagem modela as **interações locais**. Cada célula representa um indivíduo cuja evolução de saúde depende diretamente do estado de seus vizinhos, permitindo observar fenômenos espaciais como a formação de clusters e a propagação de ondas de infecção de forma muito mais realista.

## ⚙️ Parâmetros da Simulação

Você pode ajustar o comportamento da epidemia editando as variáveis no topo do arquivo `main.py`:

| Parâmetro | Descrição |
| :--- | :--- |
| `GRID_SIZE` | Dimensão da grade (ex: 50 gera uma população de 2.500 agentes). |
| `INFECTION_RATE` | Probabilidade de transmissão por contato direto com vizinho infectado. |
| `INCUBATION_PERIOD` | Tempo médio (em dias) que o agente permanece como Exposto (E). |
| `RECOVERY_RATE` | Taxa de saída do estado Infectado (I) para Recuperado ou Óbito. |
| `MORTALITY_RATE` | Probabilidade de um agente infectado progredir para Óbito (D). |

## 🎨 Representação Visual

A grade utiliza as seguintes cores para identificar o estado atual de cada agente:

| Cor | Estado | Sigla |
| :--- | :--- | :---: |
| ⬜ **Branco** | Suscetível | **S** |
| 🟨 **Amarelo** | Exposto (Incubação) | **E** |
| 🟥 **Vermelho** | Infectado (Transmissor) | **I** |
| 🟩 **Verde** | Recuperado (Imune) | **R** |
| ⬛ **Preto/Cinza** | Óbito | **D** |

## 🚀 Instalação e Uso

1. **Requisitos:** Certifique-se de ter o Python instalado.
2. **Instale as dependências:**
   ```bash
   pip install numpy matplotlib

## 📂 Estruturação de Arquivos
├── main.py              # Código principal da simulação

├── README.md            # Documentação do projeto

├── requirements.txt     # Dependências do projeto

└── artigo_tecnico.md # Detalhamento metodológico e resultados

## 🧠 Metodologia de Desenvolvimento

Este projeto foi concebido como uma demonstração técnica de **Engenharia de Software Assistida por IA**. O fluxo de trabalho simulou a atuação de um Engenheiro de Software Sênior e Especialista em Epidemiologia Computacional, utilizando a IA **Manus Lite** para a automação de ponta a ponta.

### 📜 Prompt Utilizado
O comando exato que gerou este código e documentação foi:

> "Aja como um Engenheiro de Software Sênior e Especialista em Epidemiologia Computacional. Preciso que você resolva completamente uma atividade acadêmica de modelagem de doenças infectocontagiosas. O objetivo é demonstrar como o uso de IAs permite a criação de sistemas complexos de forma automatizada.
>
> Sua tarefa consiste em gerar 4 entregáveis em uma única resposta, sem a necessidade de anexos externos:
> 1. **Código Python Completo:** Crie um código para simular o espalhamento de uma doença usando o Modelo SEIR (Suscetível, Exposto, Infectado, Removido) através de Autômatos Celulares em uma grade 2D.
> 2. **Arquivo README.md Profissional:** Escreva um arquivo de documentação para o GitHub que inclua: Título, Descrição, Instalação, Parâmetros e esta seção de Metodologia.
> 3. **Artigo Científico (Formato Markdown):** Estruturado com Resumo, Introdução, Metodologia (vizinhança de Moore/Von Neumann), Discussão de Resultados e Conclusão.
> 4. **Dados para a Planilha:** Tabela resumindo Nome do Projeto, IA Utilizada e complexidade do código.
>
> **Instruções de Formatação:** Entregue cada parte em blocos de código separados para que eu possa copiar e colar diretamente nos arquivos do GitHub."

### 🛠️ Ficha Técnica

| Atributo | Detalhes |
| :--- | :--- |
| **Projeto** | Simulação Epidemiológica SEIRD |
| **IA Utilizada** | Manus Lite |
| **Complexidade** | Alta (Modelagem Estocástica em Grade 2D) |
