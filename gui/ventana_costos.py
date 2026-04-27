import tkinter as tk
from tkinter import ttk
from src.calculadora_costos import calcular_costos

class VentanaCostos:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title("Calculadora de Costos de Importación")
        self.win.geometry("400x400")
        self.win.resizable(False, False)
        self.crear_widgets()
        self.win.transient(parent)
        self.win.grab_set()
    
    def crear_widgets(self):
        frame = ttk.Frame(self.win, padding=20)
        frame.pack(fill='both', expand=True)
        
        campos = [
            ("FOB (USD):", "fob"),
            ("Flete (USD):", "flete"),
            ("Seguro (USD):", "seguro"),
            ("Arancel (%):", "arancel"),
            ("Gastos internos (USD):", "gastos"),
            ("Margen de ganancia (%):", "margen")
        ]
        
        self.entries = {}
        for i, (texto, clave) in enumerate(campos):
            ttk.Label(frame, text=texto).grid(row=i, column=0, sticky='e', pady=3)
            entry = ttk.Entry(frame, width=20)
            entry.grid(row=i, column=1, pady=3, padx=5)
            self.entries[clave] = entry
        
        # Valores por defecto
        self.entries['fob'].insert(0, "1000")
        self.entries['flete'].insert(0, "200")
        self.entries['seguro'].insert(0, "50")
        self.entries['arancel'].insert(0, "14")
        self.entries['gastos'].insert(0, "100")
        self.entries['margen'].insert(0, "20")
        
        ttk.Button(frame, text="Calcular", command=self.calcular).grid(row=len(campos), column=0, columnspan=2, pady=15)
        
        self.resultado_texto = tk.StringVar()
        ttk.Label(frame, textvariable=self.resultado_texto, style='Result.TLabel', wraplength=350).grid(row=len(campos)+1, column=0, columnspan=2)
    
    def calcular(self):
        try:
            fob = float(self.entries['fob'].get())
            flete = float(self.entries['flete'].get())
            seguro = float(self.entries['seguro'].get())
            arancel = float(self.entries['arancel'].get())
            gastos = float(self.entries['gastos'].get())
            margen = float(self.entries['margen'].get())
            
            res = calcular_costos(fob, flete, seguro, arancel, gastos, margen)
            texto = f"CIF: ${res['CIF']}\nArancel: ${res['Arancel']}\nSubtotal: ${res['Subtotal (CIF + arancel + gastos)']}\nPrecio sugerido (margen {margen}%): ${res['Precio de venta sugerido']}"
            self.resultado_texto.set(texto)
        except ValueError:
            self.resultado_texto.set("Error: ingresá números válidos.")