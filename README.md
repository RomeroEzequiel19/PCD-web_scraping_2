# PCD-web_scraping_2

- Se deben usar la librería BeautifulSoup y requests.
- El programa primero válida si la carpeta existe y, de no ser así, se debe crear.
- Se recorren todas las etiquetas <img> de la página dada, se obtienen los enlaces src y se descargan las imágenes en la carpeta especificada, siempre y cuando sean de los formatos png,
jpg, y webp.
-Se manejan errores de conexión y descarga para asegurar que el programa no se detenga ante cualquier problema.