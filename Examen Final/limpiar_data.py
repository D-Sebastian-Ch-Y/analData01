import pandas as pd

# Cargar el dataset proporcionado para analizar su contenido
file_path = 'dataset.csv'
df = pd.read_csv(file_path)

# Limpiando los datos
data_clean = df.drop_duplicates()

# Normalizar la columna 'Categoria' (convertir a mayúsculas por si las dudas)
data_clean['Categoria'] = data_clean['Categoria'].apply(lambda x: str(x).upper())

# Normalizar valores de píxeles entre 0 y 1 (Para ayudar a los modelos)
pixel_columns = data_clean.columns[:-1]  # Excluir 'Categoria'
data_clean[pixel_columns] = data_clean[pixel_columns] / 255.0

print(data_clean)

# Guardamos el dataset limpio
data_clean.to_csv('dataset_clean.csv', index=False)