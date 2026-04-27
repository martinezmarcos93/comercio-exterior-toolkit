import tkinter as tk
from tkinter import ttk

def configurar_estilos():
    style = ttk.Style()
    style.theme_use('clam')  # moderno y multiplataforma
    
    # Colores
    bg_color = '#f0f0f0'
    fg_color = '#333333'
    btn_bg = '#4CAF50'
    btn_fg = 'white'
    
    style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Segoe UI', 10))
    style.configure('TButton', background=btn_bg, foreground=btn_fg, font=('Segoe UI', 10, 'bold'))
    style.map('TButton', background=[('active', '#45a049')])
    style.configure('TEntry', fieldbackground='white', font=('Segoe UI', 10))
    style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'))
    style.configure('Result.TLabel', font=('Segoe UI', 11, 'bold'), foreground='#2c3e50')
    style.configure('TFrame', background=bg_color)
    
    return style