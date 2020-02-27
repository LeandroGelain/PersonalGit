import spacy
from spacy_langdetect import LanguageDetector

def detectarLinguagem(texto):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
    text = str(texto)
    doc = nlp(text)
    return (doc._.language['language'])

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            print(i)
            l.append(i)
    return l