import requests
from bs4 import BeautifulSoup

def pesquisar_google(termo):
    try:
        url = f"https://www.google.com/search?q={termo.replace(' ', '+')}&hl=pt"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Pega os títulos dos resultados de busca
        resultados = [item.text for item in soup.find_all('h3')]
        return resultados[:5] if resultados else ["Nenhum resultado encontrado."]
    except requests.exceptions.RequestException as e:
        return [f"Erro ao acessar o Google: {e}"]
