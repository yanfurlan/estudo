from scraper import fetch_data
from database import create_table, insert_data

def main():
    url = 'https://example.com'
    
    # Cria a tabela se não existir
    create_table()
    
    # Raspagem dos dados
    data = fetch_data(url)
    
    # Insere os dados no banco de dados
    if data:
        insert_data(data)
        print("Dados inseridos com sucesso.")
    else:
        print("Nenhum dado encontrado.")

if __name__ == "__main__":
    main()
