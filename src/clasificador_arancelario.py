# Base de conocimiento simple (diccionario con reglas)
ARBOL = {
    "material": {
        "metal": {
            "uso": {
                "construccion": "7308.90",
                "herramienta": "8205.59",
                "otro": "7326.90"
            }
        },
        "plastico": {
            "uso": {
                "envase": "3923.10",
                "juguete": "9503.00",
                "otro": "3926.90"
            }
        },
        "textil": {
            "uso": {
                "ropa": "6204.62",
                "hogar": "6302.60",
                "otro": "6307.90"
            }
        },
        "otro": {"uso": {"general": "8479.89"}}
    }
}

def clasificar(material, uso):
    """
    Retorna un código sugerido según material y uso.
    Si no encuentra, retorna 'No clasificado'.
    """
    mat = material.lower()
    us = uso.lower()
    try:
        return ARBOL["material"].get(mat, ARBOL["material"]["otro"])["uso"].get(us, "No clasificado")
    except:
        return "No clasificado"