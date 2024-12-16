from scipy.stats import chisquare

def comparar_histo(hist1, hist2, alpha=0.05):
    # Asegúrate de que ambos diccionarios tengan las mismas claves
    todas_las_claves = set(hist1.keys()).union(set(hist2.keys()))
    
    # Extrae los valores de cada diccionario en el mismo orden de claves
    valores1 = [hist1.get(clave, 0) for clave in todas_las_claves]
    valores2 = [hist2.get(clave, 0) for clave in todas_las_claves]
    
    # Normalizar los valores para que sumen a un valor común (por ejemplo, 1 o 100)
    suma_valores1 = sum(valores1)
    suma_valores2 = sum(valores2)
    
    if suma_valores1 > 0:
        valores1 = [v / suma_valores1 for v in valores1]
    if suma_valores2 > 0:
        valores2 = [v / suma_valores2 for v in valores2]
    
    # Multiplicar por un factor más pequeño para convertir a conteos
    factor = 100  # Probar con un factor de 100 o menor
    valores1 = [v * factor for v in valores1]
    valores2 = [v * factor for v in valores2]
    
    # Realiza la prueba de chi cuadrado
    chi2_stat, p_value = chisquare(f_obs=valores1, f_exp=valores2)
    
    # valor Chi cuadrado = chi2_stat
    # P-value = p_value
    
    # Comparar el p-value con el nivel de significancia alpha
    if p_value > alpha:
        #Los histogramas son similares (no hay diferencia significativa)
        return True
    else:
        #Los histogramas son diferentes (hay diferencia significativa)
        return False
