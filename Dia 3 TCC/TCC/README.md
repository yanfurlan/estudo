# Sistema de Gerenciamento de Biblioteca

Este é um projeto simples de um sistema de gerenciamento de biblioteca, desenvolvido em Python com um banco de dados SQLite. O objetivo é demonstrar a criação e manipulação de um banco de dados, além de otimizar consultas utilizando índices.

## Estrutura do Projeto

- `insererir_dados_otimizar_consultas.py`: Script para criar o banco de dados, tabelas e inserir dados iniciais.
- `consulta_otimizada.py`: Script para realizar consultas otimizadas no banco de dados.

## Requisitos

- Python 3.6 ou superior
- SQLite

## Configuração e Execução

1. **Clone o repositório ou baixe os arquivos do projeto**:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>


2. **Crie e Popule o Banco de Dados**:

Execute o script insererir_dados_otimizar_consultas.py para criar o banco de dados, as tabelas e inserir os dados iniciais.

python insererir_dados_otimizar_consultas.py


3. **Realize Consultas Otimizadas**:

Execute o script consulta_otimizada.py para buscar livros por nome de autor.

python consulta_otimizada.py

Estrutura do Banco de Dados
    Tabela authors:

        id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
        name (TEXT, NOT NULL)

    Tabela books:
        id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
        title (TEXT, NOT NULL)
        author_id (INTEGER, FOREIGN KEY, REFERENCES authors(id))

    Funcionalidades
        Criação de tabelas authors e books.
        Inserção de registros nas tabelas.
        Criação de índice para otimização de consultas.
        Consulta de livros por nome de autor.

    Contribuição

Se você deseja contribuir com este projeto, sinta-se à vontade para enviar um pull request ou abrir uma issue.

    Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.


### Estrutura de Diretórios

O projeto deve ter a seguinte estrutura de diretórios:

biblioteca/
│
├── insererir_dados_otimizar_consultas.py
├── consulta_otimizada.py
├── README.md

Certifique-se de que todos os arquivos estejam no mesmo diretório e siga os passos descritos no README para configurar e executar o projeto.