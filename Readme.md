# 🧳 Comercio Exterior Toolkit

Conjunto de herramientas con interfaz gráfica para estudiantes de primer año de Comercio Exterior. Ideal para automatizar cálculos, consultar datos reales de divisas y commodities, analizar balanzas comerciales y generar cotizaciones profesionales.

**Desarrollado en Python con Tkinter**, pensado para ser simple de usar y fácil de extender.

---

## 📦 Funcionalidades

| Herramienta | Descripción |
|-------------|-------------|
| 🧮 **Calculadora de costos de importación** | Dado precio FOB, flete, seguro y arancel, calcula CIF, costo total y margen. |
| 💱 **Convertidor de divisas** | Obtiene tipos de cambio actualizados desde API gratuita. Permite guardar histórico. |
| 📊 **Análisis de balanza comercial** | Descarga datos del Banco Mundial y los grafica (exportaciones vs importaciones). |
| 🏷️ **Clasificador arancelario simple** | Ayuda a sugerir un código de la NCM mediante preguntas guiadas. |
| 🛢️ **Scraping de precios de commodities** | Extrae precios de sitios públicos (soja, petróleo, café) y los muestra en tabla. |
| 📄 **Generador de cotización en PDF** | Calcula costo final y emite un PDF profesional con logo y datos de la empresa. |
| 📈 **Dashboard de flujos comerciales (opcional)** | Aplicación web con Streamlit para explorar datos de exportaciones/importaciones. |

Todas las herramientas se acceden desde una **ventana principal** con botones grandes y descriptivos.

---

## 🖥️ Interfaz gráfica

![Ventana principal](docs/main_screen.png)

- **Ventana de menú** con iconos para cada módulo.
- Cada herramienta abre una **ventana independiente** con su propia lógica.
- Diseño responsivo básico, pensado para pantallas de notebook (1280x720).

---

## 📁 Estructura del proyecto

comercio-exterior-toolkit/
│
├── README.md
├── requirements.txt
├── main.py # Lanza la ventana principal
│
├── src/ # Lógica de cada herramienta
│ ├── init.py
│ ├── calculadora_costos.py
│ ├── conversor_divisas.py
│ ├── balanza_comercial.py
│ ├── clasificador_arancelario.py
│ ├── scraping_commodities.py
│ ├── generador_cotizaciones.py
│ └── streamlit_dashboard.py # (opcional, solo si se desea)
│
├── gui/ # Componentes de la interfaz gráfica
│ ├── init.py
│ ├── ventana_principal.py
│ ├── ventana_costos.py
│ ├── ventana_divisas.py
│ ├── ventana_balanza.py
│ ├── ventana_arancel.py
│ ├── ventana_commodities.py
│ ├── ventana_cotizacion.py
│ └── estilos.py # Colores, fuentes, ttk themes
│
├── data/ # Archivos generados por el usuario
│ ├── cotizaciones/ # PDFs exportados
│ ├── historico_divisas.csv
│ └── plantilla_cotizacion.png # Logo o membrete
│
└── tests/ # Pruebas unitarias (pytest)
├── test_calculadora.py
├── test_conversor.py
└── ...



---

## 🔧 Instalación

1. **Clonar el repositorio** (o descargar el ZIP)
   ```bash
   git clone https://github.com/tuusuario/comercio-exterior-toolkit.git
   cd comercio-exterior-toolkit
Crear un entorno virtual (recomendado)

bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instalar dependencias

bash
pip install -r requirements.txt
Ejecutar

bash
python main.py
Nota: El módulo de scraping y el dashboard de Streamlit pueden requerir paquetes adicionales. El requirements.txt incluye lo mínimo para las herramientas principales.

📚 Dependencias principales
Paquete	Uso
requests	Consumir APIs de divisas y descargar datos
pandas	Manejo de datos y tablas
matplotlib	Gráficos de balanza comercial
beautifulsoup4	Scraping de precios
reportlab	Generación de PDF
wbgapi	Datos del Banco Mundial
streamlit	Dashboard interactivo (opcional)
Todas las dependencias se listan en requirements.txt.

🚀 Uso rápido
Desde la interfaz gráfica
Al ejecutar main.py aparecerá la ventana principal con botones para cada herramienta. Hacé clic en la que quieras usar y seguí las instrucciones en pantalla.

Desde línea de comandos (para pruebas)
Cada módulo de src/ puede ejecutarse de forma independiente. Por ejemplo:

bash
python src/calculadora_costos.py
Esto lanzará directamente la interfaz de esa herramienta (sin el menú principal).

🧪 Pruebas
Para correr los tests:

bash
pytest tests/
Se irán agregando tests a medida que se desarrollen los módulos.

📈 Futuras mejoras
Internacionalización (inglés / portugués)

Convertidor de medidas y unidades comerciales

Integración con API de aduanas (cuando esté disponible)

Modo oscuro

Empaquetado en ejecutable (.exe) con PyInstaller

🤝 Contribuir
Si querés agregar una nueva herramienta o mejorar el código, ¡bienvenido! Hacé un fork y mandá un pull request. Revisá la guía de estilo en CONTRIBUTING.md (próximamente).

📝 Licencia
MIT – Libre para uso educativo y profesional. Consultá el archivo LICENSE.

Hecho con ❤️ para estudiantes de Comercio Exterior