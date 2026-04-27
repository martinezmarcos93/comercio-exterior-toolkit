import requests
from bs4 import BeautifulSoup

def precio_soja():
    """
    Intenta obtener el precio de la soja desde un sitio de ejemplo.
    Si falla, devuelve None.
    (Nota: esto es un esqueleto, requiere ajuste según la web real)
    """
    url = "https://www.indexmundi.com/es/precios-de-mercado/?mercancia=soja"
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        # Buscar algún elemento que contenga el precio (esto es ilustrativo)
        fila = soup.find("td", string=lambda t: "USD" in t if t else False)
        if fila:
            return fila.text.strip()
        return None
    except:
        return None