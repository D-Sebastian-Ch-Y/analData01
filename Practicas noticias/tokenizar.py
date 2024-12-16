import re
from collections import Counter

def tokenizar(lista):

    texto = ' '.join(lista)
    texto_limpio = re.sub(r'[^a-zA-Z]', '', texto).lower()
    frecuencia = Counter(texto_limpio)
    
    return frecuencia

def mostrar_dic(dic):

    for letra, conteo in dic.items():
        print(f"'{letra}': {conteo}")


def frec_rel(lista):

    frec = tokenizar(lista)
    total = 0

    for letra, conteo in frec.items():
        total += conteo
    
    for letra, conteo in frec.items():
        frec[letra] = conteo/total
    
    return dict(sorted(frec.items()))



def calcular_odd_ratios(lista):
    frecuencia = tokenizar(lista)
    total_letras = sum(frecuencia.values())
    odd_ratios = {}

    for letra, conteo in frecuencia.items():
        probabilidad = conteo / total_letras
        probabilidad_no = 1 - probabilidad
        odd_ratio = probabilidad / probabilidad_no if probabilidad_no > 0 else float('inf')
        odd_ratios[letra] = odd_ratio
    
    return odd_ratios
