# Sistema de Biblioteca

Este é um sistema de gerenciamento de biblioteca desenvolvido em Python, utilizando o ORM Peewee para gerenciamento do banco de dados SQLite.

## Requisitos

- Python 3.6 ou superior
- Peewee ORM
- SQLite3 (incluído na instalação padrão do Python)

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/TPancieri/Frameworks.git
cd Frameworks-main
```

2. Instale as dependências necessárias:
```bash
pip install peewee
```

## Configuração Inicial

Antes de executar o sistema pela primeira vez, é necessário criar o banco de dados e suas tabelas. Execute o script de criação:

```bash
python create.py
```

Este script irá:
- Criar o banco de dados SQLite (`biblioteca.db`)
- Criar todas as tabelas necessárias
- Configurar os índices e restrições

Após isso, carregue os dados iniciais do projeto. Execute o scrip de carregamento:

```bash
python load_files.py
```

## Estrutura do Projeto

```
.
├── library/                # Módulo principal da biblioteca
│   ├── __init__.py         # Exporta os modelos e conexão
│   ├── config.py           # Configuração do banco de dados
│   ├── usuario.py          # Modelo base de usuário
│   ├── cliente.py          # Modelo de cliente
│   ├── funcionario.py      # Modelo de funcionário
│   ├── livro.py            # Modelo de livro
│   └── emprestimo.py       # Modelo de empréstimo
├── crud_clientes.py        # Operações CRUD para clientes
├── crud_livros.py          # Operações CRUD para livros
├── crud_emprestimos.py     # Operações CRUD para empréstimos
├── crud_funcionarios.py    # Operações CRUD para funcionários
├── create.py               # Script de criação do banco de dados
├── load_files.py           # Utilitário para carregar dados
├── menu.py                 # Interface de menu do sistema
└── main.py                 # Ponto de entrada do programa
```

## Como Executar

1. Após a instalação e configuração inicial, execute o programa principal:

```bash
python main.py
```

2. O sistema iniciará com o menu do funcionário, onde você poderá:
   - Gerenciar clientes (cadastrar, atualizar, excluir, listar)
   - Gerenciar livros (cadastrar, atualizar, excluir, listar)
   - Gerenciar empréstimos (registrar empréstimo, registrar devolução)
   - Verificar empréstimos atrasados

## Funcionalidades

### Gerenciamento de Clientes
- Cadastro de novos clientes
- Atualização de dados
- Exclusão de clientes
- Listagem de clientes

### Gerenciamento de Livros
- Cadastro de novos livros
- Atualização de informações
- Exclusão de livros
- Listagem de livros
- Controle de disponibilidade

### Gerenciamento de Empréstimos
- Registro de empréstimos
- Registro de devoluções
- Verificação de atrasos

## Banco de Dados

O sistema utiliza SQLite como banco de dados, com as seguintes tabelas:
- `usuario`: Tabela base para usuários do sistema
- `cliente`: Herda de usuario, específica para clientes
- `funcionario`: Herda de usuario, específica para funcionários
- `livro`: Armazena informações dos livros
- `emprestimo`: Registra os empréstimos e devoluções
