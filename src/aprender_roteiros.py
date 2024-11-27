import nltk
from nltk.tokenize import sent_tokenize
from database import adicionar_resposta, obter_resposta


# Base inicial de correções (usada como fallback)
roteiro_base = {
    "escreva mais emoções": "Adicione mais descrição emocional às falas.",
    "diálogos curtos": "Simplifique os diálogos muito longos.",
    "falta de contexto": "Forneça mais contexto antes de cenas importantes."
}

def corrigir_roteiro(roteiro):
    feedbacks = []
    for chave, sugestao in roteiro_base.items():
        if chave in roteiro.lower():
            feedbacks.append(sugestao)
    
    # Adiciona feedback geral caso nada seja encontrado
    if not feedbacks:
        feedbacks.append("Nenhuma sugestão específica encontrada. O roteiro parece bom!")
    return feedbacks

def aprender_corrigir(problema, sugestao):
    roteiro_base[problema] = sugestao
    # Opcionalmente salvar no banco de dados para persistência
    adicionar_resposta(problema, sugestao)
    return f"Aprendi que '{problema}' deve ter a sugestão: '{sugestao}'."
