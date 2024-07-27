import sqlite3

def update_salary(employee_id, new_salary):
    # Conecta ao banco de dados
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Atualiza o salário do funcionário
    cursor.execute('''
    UPDATE employees
    SET salary = ?
    WHERE employee_id = ?
    ''', (new_salary, employee_id))
    
    # Salva (commit) as mudanças
    conn.commit()

    # Fecha a conexão
    conn.close()

def select_all_employees():
    # Conecta ao banco de dados
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Executa a consulta
    cursor.execute('SELECT * FROM employees')

    # Busca todos os resultados
    rows = cursor.fetchall()

    # Fecha a conexão
    conn.close()

    # Retorna os resultados
    return rows

# Atualiza o salário do funcionário com employee_id 2
update_salary(2, 48000)

# Seleciona e imprime todos os funcionários
employees = select_all_employees()
for emp in employees:
    print(emp)
