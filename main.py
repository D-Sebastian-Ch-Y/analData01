from recoger_datos import leer_datos as ld
from procesar_datos import proc_lista as pl
from procesar_datos import procesar_texto as pt
from tokenizar import tokenizar as tk
from tokenizar import frec_rel as fr
from tokenizar import calcular_odd_ratios as odd
from tokenizar import mostrar_dic as mostrar
from graficas import grafica_histograma as grafico
from graficas import graficos_acumulados as graf_ac
from graficas import graficar2 as g2
import comparar_histogramas as ch

# Creando listas de noticias por secciones
nDep = pl(ld('noticias_deporte.txt'))
nEco = pl(ld('noticias_economia.txt'))
nEnt = pl(ld('noticias_entretenimiento.txt'))
nPol = pl(ld('noticias_politica.txt'))
nSal = pl(ld('noticias_salud.txt'))
nTec = pl(ld('noticias_tecnologia.txt'))

# Verificar las letras con mejor desempeño
#graf_ac(fr(nDep), fr(nEco), fr(nEnt), fr(nPol), fr(nSal), fr(nTec))

# deportes: a l
# economia: p s
# entretenimiento: f r
# politica: d i
# salud: c u
# tecnologia: s t 

notis_eco = ["Asbanc: Tres de cada cinco peruanos en zonas urbanas gastan más de lo que ganan", "Perú y Guatemala suscribirán protocolo para viabilizar la entrada en vigencia del TLC", "Perú volverá a exportar uva de mesa a Ecuador después de ocho años"]

print(fr(nEnt))
# Primero la lista de noticias nuevas, segundo la lista de noticias de la seccion X que tengamos y por ultimo el umbral
def comp_lista(noticias, datos, umbral):
    similar = 0
    diferente = 0
    for texto in noticias:
        if(ch.comparar_histo(fr(pt(texto)), fr(datos), umbral)):
            print("SON SIMILARES")
            similar += 1
        else:
            print("SON DIFERENTES")
            diferente += 1
    print(f"De la lista de datos, con el umbral = {umbral}, {similar} histogramas son similares y {diferente} no son similares")

print("-----------------------------------------------")

comp_lista(notis_eco, nPol, 0.005)
