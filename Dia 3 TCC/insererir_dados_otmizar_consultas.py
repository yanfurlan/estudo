import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Cria uma conexão com o banco de dados SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conectado ao banco de dados: {db_file}")
    except Error as e:
        print(e)
    return conn

def execute_query(conn, query, params=None):
    """Executa uma query no banco de dados"""
    try:
        c = conn.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        conn.commit()
        print("Query executada com sucesso")
    except Error as e:
        print(e)

# Funções para inserir dados
def insert_author(conn, name):
    query = "INSERT INTO authors (name) VALUES (?)"
    execute_query(conn, query, (name,))

def insert_book(conn, title, author_id):
    query = "INSERT INTO books (title, author_id) VALUES (?, ?)"
    execute_query(conn, query, (title, author_id))

# Função para criar índices
def create_index(conn):
    index_query = "CREATE INDEX IF NOT EXISTS idx_author_id ON books (author_id)"
    execute_query(conn, index_query)

# Criar banco de dados e tabelas
database = "library.db"

conn = create_connection(database)

create_authors_table = """
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);
"""

if conn:
    execute_query(conn, create_authors_table)
    execute_query(conn, create_books_table)

    # Inserir autores
    insert_author(conn, "J.K. Rowling")
    insert_author(conn, "J.R.R. Tolkien")

    # Inserir livros
    insert_book(conn, "Harry Potter and the Philosopher's Stone", 1)
    insert_book(conn, "The Hobbit", 2)

    # Criar índice
    create_index(conn)

    # Fechar conexão
    conn.close()
