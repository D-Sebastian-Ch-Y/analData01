from sklearn.decomposition import PCA
from PIL import Image
import pandas as pd
import numpy as np
import os

carpeta_origen = "./imagenes_binarias"
cont = 0
vectores = []
categorias = []

for nombre_imagen in os.listdir(carpeta_origen):
    ruta_imagen = os.path.join(carpeta_origen, nombre_imagen)

    # Abrimos la imagen y sacamos su matriz
    imagen = Image.open(ruta_imagen)
    matriz = np.array(imagen)

    # Transformamos la imagen en un vector 1D
    vectorized_image = matriz.flatten()

    #categoria
    #os.path.splitext(nombre_imagen)[0][0]

    vectores.append(vectorized_image)
    categorias.append(os.path.splitext(nombre_imagen)[0][0])

# Crear el DataFrame
# Crear el DataFrame
df = pd.DataFrame(vectores, columns=[f'Pixel{i+1}' for i in range(780)])
df['Categoria'] = categorias  # Añadir la columna de categorías

print(df.head())

df.to_csv('dataset.csv', index=False)