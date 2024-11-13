from reconhecimento_voz import ouvir_comando
from automacao import abrir_navegador, digitar_texto
from processamento_texto import analisar_texto
from pesquisa_web import pesquisar_google

def assistente_virtual(comando=None):
    if not comando:
        comando = ouvir_comando()

    if "melhorar roteiro" in comando:
        roteiro = "Texto do roteiro a ser melhorado..."
        sugestoes = analisar_texto(roteiro)
        return f"Sugestões de melhoria: {sugestoes}"
    
    elif "abrir navegador" in comando:
        abrir_navegador()
        return "Navegador aberto com sucesso."

    elif "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip()
        resultados = pesquisar_google(termo)
        return f"Resultados da pesquisa: {resultados}"
    
    return "Comando não reconhecido. Tente novamente."