import tkinter as tk
from tkinter import ttk
from src.conversor_divisas import obtener_tasa_cambio, convertir

class VentanaDivisas:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title("Convertidor de Divisas")
        self.win.geometry("400x250")
        self.win.resizable(False, False)
        self.crear_widgets()
        self.win.transient(parent)
        self.win.grab_set()
    
    def crear_widgets(self):
        frame = ttk.Frame(self.win, padding=20)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Monto:").grid(row=0, column=0, sticky='e')
        self.monto_entry = ttk.Entry(frame, width=15)
        self.monto_entry.grid(row=0, column=1, pady=5, padx=5)
        self.monto_entry.insert(0, "100")
        
        ttk.Label(frame, text="Moneda origen:").grid(row=1, column=0, sticky='e')
        self.origen_combo = ttk.Combobox(frame, values=['USD', 'EUR', 'ARS', 'BRL'], width=10)
        self.origen_combo.current(0)
        self.origen_combo.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Moneda destino:").grid(row=2, column=0, sticky='e')
        self.destino_combo = ttk.Combobox(frame, values=['USD', 'EUR', 'ARS', 'BRL'], width=10)
        self.destino_combo.current(2)
        self.destino_combo.grid(row=2, column=1, pady=5)
        
        ttk.Button(frame, text="Convertir", command=self.convertir).grid(row=3, column=0, columnspan=2, pady=15)
        
        self.resultado_texto = tk.StringVar()
        ttk.Label(frame, textvariable=self.resultado_texto, style='Result.TLabel').grid(row=4, column=0, columnspan=2)
    
    def convertir(self):
        try:
            monto = float(self.monto_entry.get())
        except:
            self.resultado_texto.set("Monto inválido")
            return
        
        origen = self.origen_combo.get()
        destino = self.destino_combo.get()
        tasa = obtener_tasa_cambio(origen, destino)
        if tasa:
            resultado = convertir(monto, tasa)
            self.resultado_texto.set(f"{monto} {origen} = {resultado} {destino} (tasa: {tasa})")
        else:
            self.resultado_texto.set("Error al obtener tasa de cambio. Revisá internet.")