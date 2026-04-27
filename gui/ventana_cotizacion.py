import tkinter as tk
from tkinter import ttk
from src.generador_cotizaciones import generar_pdf
from datetime import date

class VentanaCotizacion:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title("Generar Cotización en PDF")
        self.win.geometry("450x500")
        self.win.resizable(False, False)
        self.crear_widgets()
        self.win.transient(parent)
        self.win.grab_set()
    
    def crear_widgets(self):
        frame = ttk.Frame(self.win, padding=20)
        frame.pack(fill='both', expand=True)
        
        campos = [
            ("Empresa:", "empresa"),
            ("Contacto:", "contacto"),
            ("Cliente:", "cliente"),
            ("Producto:", "producto"),
            ("FOB (USD):", "fob"),
            ("Flete (USD):", "flete"),
            ("Seguro (USD):", "seguro"),
            ("Arancel (%):", "arancel"),
            ("Gastos internos:", "gastos"),
            ("Margen (%):", "margen"),
            ("Validez:", "validez")
        ]
        self.entries = {}
        for i, (texto, clave) in enumerate(campos):
            ttk.Label(frame, text=texto).grid(row=i, column=0, sticky='e', pady=2)
            entry = ttk.Entry(frame, width=25)
            entry.grid(row=i, column=1, pady=2, padx=5)
            self.entries[clave] = entry
        
        self.entries['validez'].insert(0, "30 días")
        self.entries['fob'].insert(0, "1000")
        self.entries['flete'].insert(0, "200")
        self.entries['seguro'].insert(0, "50")
        self.entries['arancel'].insert(0, "14")
        self.entries['gastos'].insert(0, "100")
        self.entries['margen'].insert(0, "20")
        
        ttk.Button(frame, text="Generar PDF", command=self.generar).grid(row=len(campos), column=0, columnspan=2, pady=15)
        
        self.resultado_texto = tk.StringVar()
        ttk.Label(frame, textvariable=self.resultado_texto, style='Result.TLabel').grid(row=len(campos)+1, column=0, columnspan=2)
    
    def generar(self):
        try:
            fob = float(self.entries['fob'].get())
            flete = float(self.entries['flete'].get())
            seguro = float(self.entries['seguro'].get())
            arancel = float(self.entries['arancel'].get())
            gastos = float(self.entries['gastos'].get())
            margen = float(self.entries['margen'].get())
        except:
            self.resultado_texto.set("Error: revisá los campos numéricos.")
            return
        
        cif = fob + flete + seguro
        subtotal = cif + (cif * arancel/100) + gastos
        total = subtotal * (1 + margen/100)
        
        datos = {
            "empresa": self.entries['empresa'].get(),
            "contacto": self.entries['contacto'].get(),
            "cliente": self.entries['cliente'].get(),
            "fecha": date.today().strftime("%d/%m/%Y"),
            "producto": self.entries['producto'].get(),
            "detalle": {
                "FOB": fob,
                "Flete": flete,
                "Seguro": seguro,
                "CIF": cif,
                f"Arancel ({arancel}%)": cif * arancel/100,
                "Gastos internos": gastos,
                "Subtotal": subtotal,
                f"Margen ({margen}%)": subtotal * margen/100
            },
            "total": total,
            "validez": self.entries['validez'].get()
        }
        
        ruta = generar_pdf(datos)
        self.resultado_texto.set(f"PDF guardado en: {ruta}")