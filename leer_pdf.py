import PyPDF2


def leer_pdf(archivo_pdf): 
    # Abrir el archivo PDF en modo de lectura binaria 
    with open(archivo_pdf, 'rb') as archivo: 
        lector_pdf = PyPDF2.PdfReader(archivo) 
        texto = "" 
        
        # Recorrer todas las páginas del PDF y extraer el texto 
        for pagina in range(len(lector_pdf.pages)): 
            pagina_actual = lector_pdf.pages[pagina] 
            texto += pagina_actual.extract_text() 
    return texto

archivo_pdf = '35_82_Q1_FUNDAMENTOS DE PROGRAMACIÓN_1720077871.pdf' 
contenido = leer_pdf(archivo_pdf) 
print(contenido)