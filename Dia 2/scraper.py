import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        
        # Aqui você ajusta conforme a estrutura do site
        for item in soup.find_all('div', class_='example-class'):
            title = item.find('h2').text
            description = item.find('p').text
            data.append((title, description))
        
        return data
    else:
        print(f"Failed to retrieve data from {url}")
        return []

# Testar a função
if __name__ == "__main__":
    url = 'https://example.com'
    data = fetch_data(url)
    print(data)
