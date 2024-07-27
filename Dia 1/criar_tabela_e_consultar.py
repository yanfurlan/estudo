import sqlite3

def create_and_populate_db():
    # Conecta ao banco de dados (ou cria, se não existir)
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Cria a tabela employees
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        salary REAL,
        department_id INTEGER
    )
    ''')

    # Insere alguns registros
    employees = [
        (1, 'John', 'Doe', 60000, 10),
        (2, 'Jane', 'Smith', 45000, 20),
        (3, 'Jim', 'Beam', 55000, 10),
        (4, 'Jake', 'Blues', 30000, 30),
        (5, 'Jill', 'Valentine', 52000, 10)
    ]
    cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?)', employees)
    
    # Salva (commit) as mudanças
    conn.commit()

    # Fecha a conexão
    conn.close()

def select_high_salary_employees():
    # Conecta ao banco de dados
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Executa a consulta
    cursor.execute('''
    SELECT employee_id, first_name, last_name, salary, department_id
    FROM employees
    WHERE salary > 50000 AND department_id = 10
    ''')

    # Busca todos os resultados
    rows = cursor.fetchall()

    # Fecha a conexão
    conn.close()

    # Retorna os resultados
    return rows

# Cria e popula o banco de dados
create_and_populate_db()

# Seleciona e imprime os funcionários com salário maior que 50,000 e departamento 10
employees = select_high_salary_employees()
for emp in employees:
    print(emp)
