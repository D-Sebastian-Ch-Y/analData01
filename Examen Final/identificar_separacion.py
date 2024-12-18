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

#Leemos epicamente las imagenes con el código del profesor
images = readImg('./catchas_renombrados/')
print(f"Cantidad de imagenes que se leyó: {len(images)}")

#Creamos la matriz para sumar todos los valores de las imágenes
matriz = [[0] * 180 for _ in range(60)]
for g in images:
    matriz += g

#Sumamos las columnas para saber en cuales hay menos -> no hay letras
total = [0]*180
for fila in matriz:
    total += fila

#Nos ponemos a buscar los minimos relativos -> dónde mayormente no hay letras
minimos_relativos = []
for i in range(1, len(total) - 1):
    if total[i - 1] > total[i] < total[i + 1]:
        minimos_relativos.append(i)
print(f"Los mínimos relativos: {minimos_relativos}")

"""
A través del gráfico y la lista de minimos buscamos dónde debemos separar las imágenes
Punto 1: 8
Punto 2: 34
Punto 3: 60
Punto 4: 86
Punto 5: 112
Punto 6: 138
Punto 7: 164
separación de 26
"""
sep = [8,34,60,86,112,138,164]
for s in sep:
    plt.axvline(x=s, color='green', linestyle='--', linewidth=1)

plt.plot(total)
plt.title('Gráfica :v')
plt.xlabel('Píxeles')
plt.ylabel('Valor')
plt.show()