# 📚 Sistema de Gestão de Biblioteca (CLI)

Um sistema interativo em linha de comando (CLI) desenvolvido em **Python** para gerenciamento de acervos bibliotecários, controle de usuários e rastreamento de empréstimos e devoluções de livros com persistência em arquivos `.csv`.

---

## 📌 Visão Geral do Projeto

Este projeto foi construído para simular o funcionamento de uma biblioteca. Ele permite o cadastro centralizado de acervos e usuários, controle do status de empréstimo, consulta rápida e geração de relatórios formatados em tabela.

---

## 🛠️ Funcionalidades Principais

- **Cadastrar Livros:** Registro por código único, título e status inicial ("Disponível").
- **Cadastrar Usuários:** Registro de usuários por matrícula e nome.
- **Consultar Livros:** Busca rápida por código com exibição do responsável pelo empréstimo e data prevista de devolução.
- **Empréstimo de Livros:** Validação de existência do livro/usuário e checagem de disponibilidade antes de concluir a operação.
- **Devolução de Livros:** Restaura o status do livro para "Disponível" e limpa a alocação de usuário.
- **Relatório em Tabela:** Exibição organizada do acervo no terminal.
- **Exportação CSV:** Gravação permanente do estado atual do sistema no arquivo `relatorio_livros.csv`.

---

## 🧰 Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3.x
- **Estruturas de Dados:** Dicionários e listas para manipulação em memória.
- **Persistência:** Módulo nativo `csv` para leitura e escrita de arquivos.
- **Controle de Fluxo e Validação:** Funções modularizadas, tratamento de entradas e mensagens de erro amigáveis.

---

## 🚀 Como Executar a Aplicação

### Pré-requisitos
- **Python 3.x** instalado.

### Passo a passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/G-Eller/sistema-gestao-biblioteca.git
   cd sistema-gestao-biblioteca
   python main.py

👨‍💻 Autor
Desenvolvido por Guilherme Eller

GitHub: G-Eller
