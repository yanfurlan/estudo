import sqlite3

def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.executemany('INSERT INTO data (title, description) VALUES (?, ?)', data)
    conn.commit()
    conn.close()

# Testar a criação da tabela e inserção de dados
if __name__ == "__main__":
    create_table()
    sample_data = [('Example Title', 'Example Description')]
    insert_data(sample_data)
