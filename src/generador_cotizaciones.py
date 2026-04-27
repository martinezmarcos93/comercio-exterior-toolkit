from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os

def generar_pdf(datos, ruta_salida="data/cotizacion.pdf"):
    """
    datos: diccionario con claves:
        empresa, contacto, cliente, fecha, producto, fob, flete, seguro,
        arancel, gastos, total, validez
    """
    # Asegurar directorio
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    c = canvas.Canvas(ruta_salida, pagesize=A4)
    c.setFont("Helvetica", 12)
    
    # Cabecera
    c.drawString(30*mm, 280*mm, f"Empresa: {datos.get('empresa', 'Mi Empresa')}")
    c.drawString(30*mm, 275*mm, f"Contacto: {datos.get('contacto', '')}")
    c.drawString(30*mm, 270*mm, f"Cliente: {datos.get('cliente', '')}")
    c.drawString(30*mm, 265*mm, f"Fecha: {datos.get('fecha', '')}")
    c.drawString(30*mm, 260*mm, f"Producto: {datos.get('producto', '')}")
    
    # Línea separadora
    c.line(30*mm, 255*mm, 180*mm, 255*mm)
    
    # Detalle de costos
    y = 250*mm
    for concepto, valor in datos.get('detalle', {}).items():
        c.drawString(30*mm, y, f"{concepto}: ${valor:,.2f}")
        y -= 7*mm
    
    # Total
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30*mm, y-10*mm, f"TOTAL: ${datos.get('total', 0):,.2f}")
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y-20*mm, f"Validez: {datos.get('validez', '30 días')}")
    
    c.save()
    return ruta_salida