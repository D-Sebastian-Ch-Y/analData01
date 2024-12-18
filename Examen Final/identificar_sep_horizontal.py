import os
import cv2
import matplotlib.pyplot as plt

def readImg(path):
    images = []
    for img_name in os.listdir(path):
        filename = path + img_name

        # lee la imagen en gris
        G = cv2.imread(filename,0)
        
        #agrega la imagen a una lista
        images.append(G)

    return images

def suma_filas(images):
    matriz = [[0]*26 for _ in range(60)]
    for g in images:
        matriz += g
    total = []
    for fila in  matriz:
        total.append(sum(fila))
    return total

#Leemos epicamente las imagenes con el código del profesor y separamos
img_1 = readImg('./segmentos/1/')
total_1 = suma_filas(img_1)

img_2 = readImg('./segmentos/2/')
total_2 = suma_filas(img_2)

img_3 = readImg('./segmentos/3/')
total_3 = suma_filas(img_3)

img_4 = readImg('./segmentos/4/')
total_4 = suma_filas(img_4)

img_5 = readImg('./segmentos/5/')
total_5 = suma_filas(img_5)

img_6 = readImg('./segmentos/6/')
total_6 = suma_filas(img_6)

fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].plot(total_1, label='Acumulado del primer caracter', color='red')
axs[0].plot(total_3, label='Acumulado del tercer caracter', color='green')
axs[0].plot(total_5, label='Acumulado del quinto caracter', color='blue')
axs[0].set_title("Superposición de caracteres posición impar")
axs[0].set_xlabel("Índice")
axs[0].set_ylabel("Valor")
axs[0].legend()

axs[1].plot(total_2, label='Acumulado del segundo caracter', color='red')
axs[1].plot(total_4, label='Acumulado del cuarto caracter', color='green')
axs[1].plot(total_6, label='Acumulado del sexto caracter', color='blue')
axs[1].set_title("Superposición de caracteres posición par")
axs[1].set_xlabel("Índice")
axs[1].set_ylabel("Valor")
axs[1].legend()

plt.tight_layout()
plt.show()