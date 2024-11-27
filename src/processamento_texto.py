import spacy
from nltk.tokenize import sent_tokenize
import nltk

nltk.download("punkt")
nlp = spacy.load("pt_core_news_sm")

def analisar_texto(texto):
    try:
        doc = nlp(texto)
        # Extrai as sentenças do texto
        sugestoes = [sent.text for sent in doc.sents]

        # Realiza uma análise básica de entidades
        entidades = [(ent.text, ent.label_) for ent in doc.ents]
        
        return {
            "sentencas": sugestoes,
            "entidades": entidades
        }
    except Exception as e:
        return {"erro": f"Erro ao processar o texto: {e}"}
