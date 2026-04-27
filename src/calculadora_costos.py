def calcular_costos(fob, flete, seguro, arancel_pct, gastos_internos, margen_pct=0):
    """
    Calcula CIF, costo total, precio de venta con margen.
    Retorna un diccionario con todos los valores.
    """
    cif = fob + flete + seguro
    arancel = cif * (arancel_pct / 100)
    subtotal = cif + arancel + gastos_internos
    precio_venta = subtotal * (1 + margen_pct / 100)
    
    return {
        "CIF": round(cif, 2),
        "Arancel": round(arancel, 2),
        "Subtotal (CIF + arancel + gastos)": round(subtotal, 2),
        "Margen aplicado (%)": margen_pct,
        "Precio de venta sugerido": round(precio_venta, 2)
    }