import cv2
import os

# Configuración
carpeta_origen = "./catchas_renombrados" 
carpeta_destino = "segmentos" 
sep = [8, 34, 60, 86, 112, 138, 164]

# Crear las carpetas de destino para los segmentos
carpetas_destino = ["1", "2", "3", "4", "5", "6"]
for carpeta in carpetas_destino:
    os.makedirs(os.path.join(carpeta_destino, carpeta), exist_ok=True)

# Renombrar archivos y que se sobrescriban
def obtener_nombre_unico(carpeta_destino, nombre_segmento):
    # Generar la ruta completa del archivo
    ruta_completa = os.path.join(carpeta_destino, nombre_segmento)
    contador = 1
    
    # Si el archivo ya existe, agregar un número entre paréntesis
    base, ext = os.path.splitext(nombre_segmento)
    while os.path.exists(ruta_completa):
        # Crear un nuevo nombre con el contador
        nombre_segmento = f"{base}({contador}){ext}"
        ruta_completa = os.path.join(carpeta_destino, nombre_segmento)
        contador += 1

    return nombre_segmento

# Procesar cada imagen en la carpeta origen
for nombre_imagen in os.listdir(carpeta_origen):
    # Ruta completa de la imagen
    ruta_imagen = os.path.join(carpeta_origen, nombre_imagen)

    # Verificar si es un archivo de imagen
    if not (ruta_imagen.endswith(".jpg") or ruta_imagen.endswith(".png")):
        continue

    # Leer la imagen
    img = cv2.imread(ruta_imagen)
    if img is None:
        print(f"No se pudo leer la imagen: {nombre_imagen}")
        continue

    # Verificar que el nombre tenga al menos 6 caracteres
    base_nombre = os.path.splitext(nombre_imagen)[0]  # Quitar extensión
    if len(base_nombre) < 6:
        print(f"Nombre de archivo demasiado corto: {nombre_imagen}")
        continue

    # Cortar las 6 partes centrales (excluye las extremas)
    for i in range(len(sep) - 1):  # Ignorar el primer y último segmento
        y1, y2 = sep[i], sep[i + 1]  # Coordenadas de corte
        segmento = img[:, y1:y2]     # Segmentar verticalmente (todas las filas, columnas entre y1 y y2)

        # Usar el carácter correspondiente del nombre de la imagen
        nombre_segmento = f"{base_nombre[i]}.png"  # i para alinearse con las 6 letras de la imagen
        carpeta_segmento = carpetas_destino[i]  # Carpetas en el orden de "1", "2", "3", etc.

        # Obtener un nombre único para evitar sobrescrituras
        nombre_segmento_unico = obtener_nombre_unico(os.path.join(carpeta_destino, carpeta_segmento), nombre_segmento)

        # Ruta completa para guardar el archivo
        ruta_guardado = os.path.join(carpeta_destino, carpeta_segmento, nombre_segmento_unico)

        # Guardar el segmento
        cv2.imwrite(ruta_guardado, segmento)

print("Segmentación completada.")
