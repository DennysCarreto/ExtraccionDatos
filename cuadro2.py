import pandas as pd
import re
from PyPDF2 import PdfReader

# Primero, crea el objeto documento
ruta = '/home/dennys/Documentos/Archivos/Analisis Anual 2018 ETAS.pdf'
documento = PdfReader(ruta)

# Ahora puedes acceder a la página que necesitas
pagina = documento.pages[3]
texto = pagina.extract_text()

patron = r'(\d{4})\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+%)\s+\((\d+)/(\d+)\)'
datos = re.findall(patron, texto)

cuadro2 = pd.DataFrame(datos, columns=['Año', 'Reportados', 'Investigados', 'Informados', 'Porcentaje Notificación', 'DAS Notificadas', 'Total DAS'])

# Convertir tipos de datos
cuadro2['Año'] = cuadro2['Año'].astype(int)
cuadro2['Reportados'] = cuadro2['Reportados'].astype(int)
cuadro2['Investigados'] = cuadro2['Investigados'].astype(int)
cuadro2['Informados'] = cuadro2['Informados'].astype(int)
cuadro2['DAS Notificadas'] = cuadro2['DAS Notificadas'].astype(int)
cuadro2['Total DAS'] = cuadro2['Total DAS'].astype(int)

print(cuadro2)