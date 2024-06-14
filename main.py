import requests
from bs4 import BeautifulSoup
import os

# Crear la carpeta para colocar las imágenes
def crear_carpeta(dir):

    if os.path.exists(dir):
        print("La carpeta de Imágenes ya está creada")

    else:
        try:
            os.mkdir(dir)
        except OSError:
            print("La creación del directorio %s falló" % dir)
        else:
            print("Se ha creado el directorio: %s " % dir)

# Obtener las imágenes
def obtener_imagenes(url):

    imagenes = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("img")

    for img in results:
        imagenes.append(img)
    return imagenes

# Obtener las url de las imagenes
def obtener_url(imagenes):
    extensiones_utilizar = ["png", "jpg", "webp"]
    urls_correctas = []

    for img in imagenes:
        src = img.get("src")
        extension_src = src.split(".")[-1].lower()

        if extension_src in extensiones_utilizar:
            urls_correctas.append(src)

    return urls_correctas

def cargar_en_carpeta(urls, dir):
    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            response.raise_for_status()
            extension = url.split(".")[-1]
            with open(os.path.join(dir, f"imagen_{i}.{extension}"), 'wb') as file:
                file.write(response.content)
            print(f"Imagen {i} guardada en {dir}")
        except requests.RequestException as e:
            print(f"Error al descargar la imagen de {url}: {e}")

url = "https://www.bbc.com/mundo/topics/cyx5krnw38vt"
directorio = "./imagenes"
crear_carpeta(directorio)
imagenes = obtener_imagenes(url)
url_correctas = obtener_url(imagenes)
cargar_en_carpeta(url_correctas, directorio)