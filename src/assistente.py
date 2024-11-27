from reconhecimento_voz import ouvir_comando
from automacao import abrir_pasta, abrir_site
from processamento_texto import analisar_texto
from pesquisa_web import pesquisar_google
from aprender_roteiros import corrigir_roteiro, aprender_corrigir
from database import criar_tabela, obter_resposta, adicionar_resposta

# Inicialize a base de dados
criar_tabela()

def assistente_virtual(comando):
    comando = comando.lower()  # Padronizar para minúsculas

    # Responder ou corrigir roteiros
    if "corrigir roteiro" in comando:
        roteiro = comando.replace("corrigir roteiro", "").strip()
        sugestoes = corrigir_roteiro(roteiro)
        return "Sugestões de melhoria: " + "; ".join(sugestoes)
    
    if "ensinar roteiro" in comando:
        partes = comando.split("ensinar roteiro", 1)[1].strip().split(":", 1)
        if len(partes) == 2:
            problema, sugestao = partes
            aprender_corrigir(problema.strip(), sugestao.strip())
            return f"Aprendi a sugerir: '{sugestao.strip()}' para o problema '{problema.strip()}'."
        return "Não entendi como ensinar roteiro. Use o formato: ensinar roteiro problema:sugestão"

    # Automação de Tarefas
    if "abrir pasta" in comando:
        caminho = comando.replace("abrir pasta", "").strip()
        abrir_pasta(caminho)
        return f"Abri a pasta: {caminho}"

    if "abrir site" in comando:
        partes = comando.split("abrir site", 1)
        if len(partes) > 1:
            url = partes[1].strip()
            abrir_site(url, navegador="chrome")
            return f"Site {url} aberto no Chrome."
        return "Você precisa especificar o site para abrir. Exemplo: abrir site google.com"

    # Pesquisar na web
    if "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip()
        resultados = pesquisar_google(termo)
        return "Aqui estão os 5 principais resultados: " + "; ".join(resultados)

    # Aprendizado básico
    if "ensinar" in comando:
        partes = comando.split("ensinar", 1)[1].strip().split(":", 1)
        if len(partes) == 2:
            pergunta, resposta = partes
            adicionar_resposta(pergunta.strip(), resposta.strip())
            return f"Entendido! Vou lembrar que '{pergunta.strip()}' tem como resposta '{resposta.strip()}'."
        return "Não entendi como ensinar. Use o formato: ensinar pergunta:resposta"

    # Resposta padrão
    resposta = obter_resposta(comando)
    if resposta:
        return resposta

    return "Desculpe, ainda não sei responder isso. Você pode me ensinar?"
