from recoger_datos import leer_datos as ld
from procesar_datos import proc_lista as pl
from tokenizar import tokenizar as tk
from tokenizar import frec_rel as fr
from tokenizar import calcular_odd_ratios as odd
from tokenizar import mostrar_dic as mostrar
from graficas import grafica_histograma as grafico
from graficas import graficos_acumulados as graf_ac

# Creando listas de noticias por secciones
nDep = pl(ld('noticias_deporte.txt'))
nEco = pl(ld('noticias_economia.txt'))
nEnt = pl(ld('noticias_entretenimiento.txt'))
nPol = pl(ld('noticias_politica.txt'))
nSal = pl(ld('noticias_salud.txt'))
nTec = pl(ld('noticias_tecnologia.txt'))

# Verificar las letras con mejor desempeño
graf_ac(fr(nDep), fr(nEco), fr(nEnt), fr(nPol), fr(nSal), fr(nTec))

# deportes: a l
# economia: p
# entretenimiento: f r
# politica: d i
# salud: c u
# tecnologia: s t  [a]