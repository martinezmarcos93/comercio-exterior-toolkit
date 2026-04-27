import tkinter as tk
from tkinter import ttk
from src.clasificador_arancelario import clasificar

class VentanaArancel:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title("Clasificador Arancelario Simple")
        self.win.geometry("400x300")
        self.win.resizable(False, False)
        self.crear_widgets()
        self.win.transient(parent)
        self.win.grab_set()
    
    def crear_widgets(self):
        frame = ttk.Frame(self.win, padding=20)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Material:").grid(row=0, column=0, sticky='e')
        self.material_combo = ttk.Combobox(frame, values=['metal', 'plastico', 'textil', 'otro'], state='readonly')
        self.material_combo.current(0)
        self.material_combo.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Uso:").grid(row=1, column=0, sticky='e')
        self.uso_combo = ttk.Combobox(frame, values=['construccion', 'herramienta', 'envase', 'juguete', 'ropa', 'hogar', 'general', 'otro'], state='readonly')
        self.uso_combo.current(0)
        self.uso_combo.grid(row=1, column=1, pady=5)
        
        ttk.Button(frame, text="Clasificar", command=self.clasificar).grid(row=2, column=0, columnspan=2, pady=15)
        
        self.resultado_texto = tk.StringVar()
        ttk.Label(frame, textvariable=self.resultado_texto, style='Result.TLabel', font=('Segoe UI', 16, 'bold')).grid(row=3, column=0, columnspan=2)
    
    def clasificar(self):
        material = self.material_combo.get()
        uso = self.uso_combo.get()
        codigo = clasificar(material, uso)
        self.resultado_texto.set(f"Código sugerido: {codigo}")