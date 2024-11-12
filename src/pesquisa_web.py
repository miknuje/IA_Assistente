import requests
from bs4 import BeautifulSoup

def pesquisar_google(termo):
    url = f"https://www.google.com/search?q={termo.replace(' ', '+')}&hl=pt"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    resultados = [item.text for item in soup.find_all('h3')]
    return resultados[:5]