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

# Função para buscar livros por autor
def get_books_by_author(conn, author_name):
    query = """
    SELECT books.title FROM books
    JOIN authors ON books.author_id = authors.id
    WHERE authors.name = ?
    """
    return fetch_query(conn, query, (author_name,))

# Conectar ao banco e buscar livros por autor
database = "library.db"
conn = create_connection(database)

books = get_books_by_author(conn, "J.K. Rowling")
for book in books:
    print(book[0])

# Fechar conexão
conn.close()
