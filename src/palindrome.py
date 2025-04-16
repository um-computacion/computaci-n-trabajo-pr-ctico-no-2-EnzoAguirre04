# Trabajo Práctico 2: Desarrollo Guiado por Pruebas (TDD) - Detector de Palíndromos
# Nombre y Apellido: Enzo Aguirre

import unicodedata

def is_palindrome(text):
    # Normalizar: quitar tildes y diacríticos
    text = unicodedata.normalize('NFKD', text)
    # Eliminar todo lo que no sea alfanumérico (sin tildes) y convertir a minúsculas
    cleaned_text = ''.join(
        c for c in text if c.isalnum() and not unicodedata.combining(c)
    ).lower()
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    print("Inicio del programa. Usa Ctrl+C para salir.\n")

    try:
        while True:
            text = input("Introduce un texto para verificar si es un palíndromo: ").strip()
            if is_palindrome(text):
                print("Es un palíndromo.")
            else:
                print("No es un palíndromo.")
    except KeyboardInterrupt:
        print("\n\nFin del programa. ¡Hasta luego!")