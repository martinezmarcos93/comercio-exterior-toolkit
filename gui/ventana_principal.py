import tkinter as tk
from tkinter import ttk
from gui.estilos import configurar_estilos
from gui.ventana_costos import VentanaCostos
from gui.ventana_divisas import VentanaDivisas
from gui.ventana_balanza import VentanaBalanza
from gui.ventana_arancel import VentanaArancel
from gui.ventana_commodities import VentanaCommodities
from gui.ventana_cotizacion import VentanaCotizacion

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Comercio Exterior Toolkit")
        self.root.geometry("600x500")
        configurar_estilos()
        
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        ttk.Label(main_frame, text="Herramientas para Comercio Exterior", style='Header.TLabel').pack(pady=20)
        
        botones = [
            ("🧮 Calculadora de costos", self.abrir_costos),
            ("💱 Convertidor de divisas", self.abrir_divisas),
            ("📊 Balanza comercial", self.abrir_balanza),
            ("🏷️ Clasificador arancelario", self.abrir_arancel),
            ("🛢️ Precios commodities", self.abrir_commodities),
            ("📄 Generar cotización PDF", self.abrir_cotizacion),
        ]
        
        for texto, comando in botones:
            btn = ttk.Button(main_frame, text=texto, command=comando)
            btn.pack(fill='x', pady=5, ipady=5)
        
        ttk.Label(main_frame, text="Seleccioná una herramienta para empezar", style='TLabel').pack(pady=15)
    
    def abrir_costos(self):
        VentanaCostos(self.root)
    
    def abrir_divisas(self):
        VentanaDivisas(self.root)
    
    def abrir_balanza(self):
        VentanaBalanza(self.root)
    
    def abrir_arancel(self):
        VentanaArancel(self.root)
    
    def abrir_commodities(self):
        VentanaCommodities(self.root)
    
    def abrir_cotizacion(self):
        VentanaCotizacion(self.root)