import spacy
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")
nlp = spacy.load("pt_core_news_sm")

def analisar_texto(texto):
    doc = nlp(texto)
    sugestoes = [sent.text for sent in doc.sents]
    return sugestoes