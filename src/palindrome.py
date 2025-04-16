# Trabajo Práctico 2: Desarrollo Guiado por Pruebas (TDD) - Detector de Palíndromos
# Nombre y Apellido: Enzo Aguirre

def is_palindrome(text):
    cleaned_text = ''.join(char for char in text.lower() if char.isalnum())
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