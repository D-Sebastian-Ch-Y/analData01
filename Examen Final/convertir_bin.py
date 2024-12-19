from PIL import Image
import os

carpeta_destino = "imagenes_binarias"
os.makedirs(os.path.join(carpeta_destino), exist_ok=True)

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

def convertir_bin(carpeta_origen):
    cont = 0
    for nombre_imagen in os.listdir(carpeta_origen): 
        cont += 1

        ruta_imagen = os.path.join(carpeta_origen, nombre_imagen)

        # Abrimos la imagen
        imagen = Image.open(ruta_imagen)

        # Convertimos a escala de grises
        imagen_gris = imagen.convert('L')

        # Definimos un umbral, por prueba y error nos quedamos con 128
        umbral = 128
        imagen_binaria = imagen_gris.point(lambda p: p > umbral and 255)

        # Quitar extensión para guardar el carácter del inicio
        nombre_base = f"{os.path.splitext(nombre_imagen)[0][0]}.png"
        nombre_unico = obtener_nombre_unico(carpeta_destino, nombre_base)
        ruta_guardado = os.path.join(carpeta_destino, nombre_unico)
        # Guarda la imagen binaria
        imagen_binaria.save(ruta_guardado)

    print(f"Se convirtieron {cont} imagenes a imagenes binarias de la carpeta {carpeta_origen}")
    return


convertir_bin('./segmentos/1/')
convertir_bin('./segmentos/2/')
convertir_bin('./segmentos/3/')
convertir_bin('./segmentos/4/')
convertir_bin('./segmentos/5/')
convertir_bin('./segmentos/6/')