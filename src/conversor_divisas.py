import requests

def obtener_tasa_cambio(moneda_origen="USD", moneda_destino="ARS"):
    """
    Obtiene el tipo de cambio actual usando la API gratuita de Frankfurter.
    Si falla, retorna None.
    """
    url = f"https://api.frankfurter.app/latest?from={moneda_origen}&to={moneda_destino}"
    try:
        respuesta = requests.get(url, timeout=5)
        datos = respuesta.json()
        return datos["rates"][moneda_destino]
    except Exception:
        return None

def convertir(monto, tasa):
    if tasa is None:
        return None
    return round(monto * tasa, 2)