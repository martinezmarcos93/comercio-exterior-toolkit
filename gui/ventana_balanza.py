import tkinter as tk
from tkinter import ttk
from src.balanza_comercial import descargar_datos_balanza, graficar_balanza
import threading

class VentanaBalanza:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title("Análisis de Balanza Comercial")
        self.win.geometry("800x600")
        self.crear_widgets()
        self.win.transient(parent)
        self.win.grab_set()
    
    def crear_widgets(self):
        frame = ttk.Frame(self.win, padding=10)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Países (separados por coma):").grid(row=0, column=0, sticky='e')
        self.paises_entry = ttk.Entry(frame, width=30)
        self.paises_entry.insert(0, "ARG,BRA,CHL")
        self.paises_entry.grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Button(frame, text="Descargar y graficar", command=self.descargar).grid(row=0, column=2, padx=5)
        
        self.grafico_frame = ttk.Frame(frame)
        self.grafico_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky='nsew')
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        
        self.estado = tk.StringVar(value="Listo")
        ttk.Label(frame, textvariable=self.estado).grid(row=2, column=0, columnspan=3)
    
    def descargar(self):
        paises = [p.strip().upper() for p in self.paises_entry.get().split(",")]
        self.estado.set("Descargando...")
        # Ejecutar en hilo para no congelar la interfaz
        threading.Thread(target=self._descargar_thread, args=(paises,), daemon=True).start()
    
    def _descargar_thread(self, paises):
        try:
            df = descargar_datos_balanza(paises)
            # Actualizar gráfico en el hilo principal
            self.win.after(0, self.mostrar_grafico, df)
            self.win.after(0, self.estado.set, "Gráfico listo"))
        except Exception as e:
            self.win.after(0, self.estado.set, f"Error: {e}")
    
    def mostrar_grafico(self, df):
        graficar_balanza(df, self.grafico_frame)