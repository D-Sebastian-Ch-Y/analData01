import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

# ejemplo url: https://larepublica.pe/salud
def LR_data(url):
    
    articulos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('a', class_='extend-link')

        for title in titles:
            articulos.append(title.get_text(strip=True))
    else:
        print("Error al acceder a la página la republica:", response.status_code)

    return articulos

# ejemplo url: https://trome.com/actualidad/economia/
def TR_data(url):

    articulos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('a', class_='story-grid__title block overflow-hidden mt-10')

        for title in titles:
            articulos.append(title.get_text(strip=True))
    else:
        print("Error al acceder a la página trome:", response.status_code)
    
    return articulos

# ejemplo de url: https://rpp.pe/vital/salud
def RPP_data(url):

    articulos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2', class_='news__title')

        for title in titles:
            articulos.append(title.get_text(strip=True))
    else:
        print("Error al acceder a la página:", response.status_code)
    
    return articulos

# ejemplo de url: https://www.infobae.com/tag/peru-entretenimiento/
def INF_data(url):

    articulos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2', class_='feed-list-card-headline-lean')

        for title in titles:
            articulos.append(title.get_text(strip=True))
    else:
        print("Error al acceder a la página:", response.status_code)

    return articulos

# ejemplo de url: https://www.americatv.com.pe/entretenimiento 
def ATV_data(url, sec):
    
    articulos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if sec == "salud":
            titles = soup.find_all('h3', class_='CardUei_title__yMyUo')
        elif sec == "deportes":
            titles = soup.find_all('h3', class_='CardPrimary_tinu__MQM3J')
        elif sec == "entretenimiento":
            titles = soup.find_all('a', class_='font-bold text-xl')
        elif sec == "tecnologia":
            titles = soup.find_all('h3', class_='CardUei_title__yMyUo')
        else:
            print("Sección no disponible en AmericaTV")

        for title in titles:
            articulos.append(title.get_text(strip=True))
    else:
        print("Error al acceder a la página:", response.status_code)

    return articulos

# ejemplo de url: https://lpderecho.pe/category/economia/
def LPD_data(url):

    articulos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3', class_='entry-title td-module-title')

        for title in titles:
            articulos.append(title.get_text(strip=True))
    else:
        print("Error al acceder a la página:", response.status_code)
    
    return articulos

notis_politica = LR_data("https://larepublica.pe/politica") + INF_data("https://www.infobae.com/tag/peru-politica/") + RPP_data("https://rpp.pe/politica") + TR_data("https://trome.com/actualidad/politica/") + LPD_data("https://lpderecho.pe/category/procesal-civil-2/")
notis_deporte = LR_data("https://larepublica.pe/deportes") + INF_data("https://www.infobae.com/peru/deportes/") + RPP_data("https://rpp.pe/deportes") + TR_data("https://trome.com/deportes/") + ATV_data("https://www.americatv.com.pe/deportes/futbol-peruano", "deportes") + ATV_data("https://www.americatv.com.pe/deportes/futbol-peruano", "deportes")
notis_entretenimiento = INF_data("https://www.infobae.com/tag/peru-entretenimiento/") + RPP_data("https://rpp.pe/entretenimiento") + LR_data("https://larepublica.pe/entretenimiento") + ATV_data("https://www.americatv.com.pe/entretenimiento", "entretenimiento") + LPD_data("https://lpderecho.pe/category/humor/")
notis_economia = INF_data("https://www.infobae.com/tag/peru-economia/") + RPP_data("https://rpp.pe/economia") + LR_data("https://larepublica.pe/economia") + TR_data("https://trome.com/actualidad/economia/") + LPD_data("https://lpderecho.pe/category/economia/")
notis_salud = RPP_data("https://rpp.pe/vital/salud") + LR_data("https://larepublica.pe/salud") + TR_data("https://trome.com/familia/salud/") + ATV_data("https://www.americatv.com.pe/noticias/util-e-interesante/salud", "salud") + LPD_data("https://lpderecho.pe/category/seguros/")
notis_tecnologia = RPP_data("https://rpp.pe/tecnologia") + RPP_data("https://rpp.pe/tecnologia/pc") + LR_data("https://larepublica.pe/tecnologia") + TR_data("https://trome.com/tecnologia/internet/") + TR_data("https://trome.com/tecnologia/videojuegos/") + TR_data("https://trome.com/tecnologia/smartphones/") + TR_data("https://trome.com/tecnologia/apps/") + ATV_data("https://www.americatv.com.pe/noticias/util-e-interesante/tecnologia", "tecnologia")


def guardar_datos(lista, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for item in lista:
            f.write(f"{item}\n")

guardar_datos(notis_politica, 'noticias_politica.txt')
guardar_datos(notis_deporte, 'noticias_deporte.txt')
guardar_datos(notis_entretenimiento, 'noticias_entretenimiento.txt')
guardar_datos(notis_economia, 'noticias_economia.txt')
guardar_datos(notis_salud, 'noticias_salud.txt')
guardar_datos(notis_tecnologia, 'noticias_tecnologia.txt')

def leer_datos(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            lista.append(linea.strip())
    return lista