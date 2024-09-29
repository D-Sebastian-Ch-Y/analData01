import numpy as np
import matplotlib.pyplot as plt

def grafica_histograma(frecuencias_relativas):

    categorias = list(frecuencias_relativas.keys())
    valores = list(frecuencias_relativas.values())

    plt.bar(categorias, valores)

    plt.title('Histograma de Frecuencias Relativas')
    plt.xlabel('Categorías')
    plt.ylabel('Frecuencias Relativas')

    plt.show()


def graficos_acumulados(frecuencias_relativas_1,frecuencias_relativas_2,frecuencias_relativas_3,frecuencias_relativas_4,frecuencias_relativas_5,frecuencias_relativas_6):
    
    # Extraer claves y valores
    categorias = list(frecuencias_relativas_1.keys())
    valores_1 = list(frecuencias_relativas_1.values())
    valores_2 = list(frecuencias_relativas_2.values())
    valores_3 = list(frecuencias_relativas_3.values())
    valores_4 = list(frecuencias_relativas_4.values())
    valores_5 = list(frecuencias_relativas_5.values())
    valores_6 = list(frecuencias_relativas_6.values())

    # Configuración para el gráfico
    x = np.arange(len(categorias))  # la posición de las categorías
    ancho = 0.1  # ancho de las barras

    # Crear el gráfico de barras agrupadas
    fig, ax = plt.subplots()
    barras_1 = ax.bar(x - 2.5*ancho, valores_1, ancho, label='Conjunto 1')
    barras_2 = ax.bar(x - 1.5*ancho, valores_2, ancho, label='Conjunto 2')
    barras_3 = ax.bar(x - 0.5*ancho, valores_3, ancho, label='Conjunto 3')
    barras_4 = ax.bar(x + 0.5*ancho, valores_4, ancho, label='Conjunto 4')
    barras_5 = ax.bar(x + 1.5*ancho, valores_5, ancho, label='Conjunto 5')
    barras_6 = ax.bar(x + 2.5*ancho, valores_6, ancho, label='Conjunto 6')

    # Añadir título y etiquetas
    ax.set_title('Comparación de Frecuencias Relativas')
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Frecuencias Relativas')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Mostrar el gráfico
    plt.tight_layout()  # Ajustar el diseño para que no se solapen las etiquetas
    plt.show()

def graficar2(frecuencias_relativas_1,frecuencias_relativas_2):
    # Unir las claves
    categorias = sorted(set(frecuencias_relativas_1.keys()).union(set(frecuencias_relativas_2.keys())))

    # Crear listas de frecuencias alineadas
    valores_1 = [frecuencias_relativas_1.get(cat, 0) for cat in categorias]
    valores_2 = [frecuencias_relativas_2.get(cat, 0) for cat in categorias]

    # Configuración para el gráfico
    x = np.arange(len(categorias))  # la posición de las categorías
    ancho = 0.35  # ancho de las barras

    # Crear el gráfico de barras agrupadas
    fig, ax = plt.subplots()
    barras_1 = ax.bar(x - ancho/2, valores_1, ancho, label='Conjunto 1')
    barras_2 = ax.bar(x + ancho/2, valores_2, ancho, label='Conjunto 2')

    # Añadir título y etiquetas
    ax.set_title('Comparación de Frecuencias Relativas')
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Frecuencias Relativas')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Mostrar el gráfico
    plt.show()
        