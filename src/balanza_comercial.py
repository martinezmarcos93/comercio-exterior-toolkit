import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def descargar_datos_balanza(paises, desde=2010, hasta=2022):
    """
    Descarga exportaciones (NE.EXP.GNFS.CD) e importaciones (NE.IMP.GNFS.CD)
    para una lista de países.
    Retorna un DataFrame con columnas: país, año, Indicador, valor.
    """
    indicadores = ['NE.EXP.GNFS.CD', 'NE.IMP.GNFS.CD']
    df = wb.data.DataFrame(indicadores, economy=paises, time=range(desde, hasta+1))
    df = df.reset_index()
    df = df.melt(id_vars=['economy', 'time'], var_name='Indicador', value_name='Valor')
    df = df.rename(columns={'economy': 'Pais', 'time': 'Año'})
    return df.dropna()

def graficar_balanza(df, frame_grafico):
    """
    Dibuja el gráfico dentro de un frame de Tkinter.
    """
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    for pais in df['Pais'].unique():
        datos = df[df['Pais'] == pais]
        for indicador in ['NE.EXP.GNFS.CD', 'NE.IMP.GNFS.CD']:
            subset = datos[datos['Indicador'] == indicador]
            etiqueta = f"{pais} - {'Export' if 'EXP' in indicador else 'Import'}"
            ax.plot(subset['Año'], subset['Valor'], marker='o', label=etiqueta)
    
    ax.set_title("Balanza Comercial")
    ax.set_xlabel("Año")
    ax.set_ylabel("USD corrientes")
    ax.legend()
    ax.grid(True)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)