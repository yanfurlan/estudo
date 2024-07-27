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

def fetch_query(conn, query, params=None):
    """Executa uma query SELECT e retorna os resultados"""
    try:
        c = conn.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        return c.fetchall()
    except Error as e:
        print(e)
        return []

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

# Fechar conexão
conn.close()
