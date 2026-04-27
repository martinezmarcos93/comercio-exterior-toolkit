import tkinter as tk
from tkinter import ttk
from src.scraping_commodities import precio_soja

class VentanaCommodities:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title("Precios de Commodities")
        self.win.geometry("400x200")
        self.win.resizable(False, False)
        self.crear_widgets()
        self.win.transient(parent)
        self.win.grab_set()
    
    def crear_widgets(self):
        frame = ttk.Frame(self.win, padding=20)
        frame.pack(fill='both', expand=True)
        
        ttk.Button(frame, text="Consultar precio de soja", command=self.consultar).pack(pady=20)
        
        self.resultado_texto = tk.StringVar(value="Presione para consultar")
        ttk.Label(frame, textvariable=self.resultado_texto, style='Result.TLabel').pack()
    
    def consultar(self):
        precio = precio_soja()
        if precio:
            self.resultado_texto.set(f"Precio soja: {precio}")
        else:
            self.resultado_texto.set("No se pudo obtener el precio (verifique conexión o sitio fuente)")