import leer_pdf

if __name__ == "__main__":
    archivo_pdf = "\pdf\35_82_Q1_FUNDAMENTOS DE PROGRAMACIÓN_1720077871.pdf"
    archivo_json = "resultado.json"

    # Leer el contenido del PDF
    texto_pdf = leer_pdf(archivo_pdf)
    print(texto_pdf)

    # Convertir el contenido del PDF a JSON
    #contenido_json = convertir_a_json(texto_pdf)

    # Guardar el JSON en un archivo
    #guardar_json(archivo_json, contenido_json)

    #print(f"El contenido del PDF ha sido convertido a JSON y guardado en {archivo_json}")
