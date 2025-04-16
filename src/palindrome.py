# Trabajo Práctico 2: Desarrollo Guiado por Pruebas (TDD) - Detector de Palíndromos
# Nombre y Apellido: Enzo Aguirre

def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    print("Incio del programa escriba 'Fin', para finalizarlo.")

    while True:
        text = input("Introduce un texto para verificar si es un palíndromo: ").strip().lower()
        if text in ["'fin'", "'fin", "fin'", "fin"]:
            break
        elif is_palindrome(text):
            print("Es un palíndromo.")
        else:
            print("No es un palíndromo.")

    print("Fin del programa.")