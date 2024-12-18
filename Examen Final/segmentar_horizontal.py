import os
import cv2
import matplotlib.pyplot as plt

def readImg(path):
    images = []
    nombres = []
    for img_name in os.listdir(path):
        filename = path + img_name

        # lee la imagen en gris
        G = cv2.imread(filename,0)
        
        #agrega la imagen a una lista y los nombres de la ruta de donde salieron
        images.append(G)
        nombres.append(filename)

    return images, nombres

def recortar_h(carpeta, y1, y2):
    lista_img, list_nom = readImg(carpeta)
    i = 0
    camb = 0
    n_camb = 0

    for img in lista_img:
        if(len(img)>(y2-y1)):
            new_img = img[y1:y2, :] 
            cv2.imwrite(list_nom[i], new_img)
            camb += 1
        else:
            n_camb += 1
        i += 1
    print(f"Se cambiaron {camb} archivos de tamaño y {n_camb} no se alteraron, de un total de {camb+n_camb} archivos en la carpeta {carpeta}")
    return

"""
A través del gráfico de "identificar_sep_horizontal.py" debemos cortar las imagenes de la siguiente forma:
Segmentos 1: de 10 a 40
Segmentos 2: de 20 a 50
Segmentos 3: de 10 a 40
Segmentos 4: de 20 a 50
Segmentos 5: de 10 a 40
Segmentos 6: de 20 a 50

"""


#segmentar las imagenes en horizontal
recortar_h('./segmentos/1/', 10, 40)
recortar_h('./segmentos/3/', 10, 40)
recortar_h('./segmentos/5/', 10, 40)

recortar_h('./segmentos/2/', 20, 50)
recortar_h('./segmentos/4/', 20, 50)
recortar_h('./segmentos/6/', 20, 50)
