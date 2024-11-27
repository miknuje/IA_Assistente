import os
import webbrowser

def abrir_pasta(caminho):
    try:
        os.startfile(caminho)  # Apenas para Windows
    except Exception as e:
        print(f"Erro ao abrir a pasta: {e}")

def abrir_site(url, navegador="chrome"):
    if navegador == "chrome":
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    elif navegador == "edge":
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        webbrowser.get(edge_path).open(url)
    else:
        webbrowser.open(url)
