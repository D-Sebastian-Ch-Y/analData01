import unicodedata
import re

def procesar_texto(texto):
        
    texto = texto.replace('Ñ', '').replace('Ç', '')
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(char for char in texto if unicodedata.category(char) != 'Mn')
    texto = texto.upper()
    texto = re.sub(r'[^A-Z0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto

def proc_lista(lista):
    
    return [procesar_texto(texto) for texto in lista]




