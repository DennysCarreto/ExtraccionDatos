import pandas as pd
import re
from PyPDF2 import PdfReader

# Crear el objeto documento
ruta = '/home/dennys/Documentos/Archivos/Analisis Anual 2018 ETAS.pdf'
documento = PdfReader(ruta)

# Acceder a la página que contiene el Cuadro 3
pagina = documento.pages[4] 
texto = pagina.extract_text()

# Patrón para extraer los datos del Cuadro 3
patron = r'(\d+)\s+(\d+)\s+([\w\s-]+?)\s+([\w\s]+?)\s+([\w\s,]+?)\s+(\d+)(?=\n\d+|\Z)'
datos = re.findall(patron, texto)

# Crear el DataFrame
cuadro3 = pd.DataFrame(datos, columns=['No.', 'SE', 'Area de Salud', 'ETA reportada', 'Fuente de Contagio', 'No. De casos'])

# Tipos de datos
cuadro3['No.'] = cuadro3['No.'].astype(int)
cuadro3['SE'] = cuadro3['SE'].astype(int)
cuadro3['No. De casos'] = cuadro3['No. De casos'].astype(int)

# Espacios en blanco extra
cuadro3['Area de Salud'] = cuadro3['Area de Salud'].str.strip()
cuadro3['ETA reportada'] = cuadro3['ETA reportada'].str.strip()
cuadro3['Fuente de Contagio'] = cuadro3['Fuente de Contagio'].str.strip()

print(cuadro3)