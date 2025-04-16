# Trabajo Práctico 2: Desarrollo Guiado por Pruebas (TDD) - Detector de Palíndromos
# Nombre y Apellido: Enzo Aguirre

import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("anilina"))
        self.assertTrue(is_palindrome("menem"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("somos"))
        self.assertTrue(is_palindrome("deified"))
        self.assertTrue(is_palindrome("rotator"))
        self.assertTrue(is_palindrome("civic"))
        self.assertTrue(is_palindrome("refer"))
        self.assertTrue(is_palindrome("noon"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama."))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon."))
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_palindrome("Mr. Owl ate my metal worm."))
        self.assertTrue(is_palindrome("Anita lava la tina."))
        self.assertTrue(is_palindrome("A mamá Roma le aviva el amor a mamá."))
        self.assertTrue(is_palindrome("La ruta natural."))
        self.assertTrue(is_palindrome("La ruta nos aportó otro paso natural."))
        self.assertTrue(is_palindrome("Anita atina la palapa latina."))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome."))
        self.assertFalse(is_palindrome("planet"))
        self.assertFalse(is_palindrome("computer"))
        self.assertFalse(is_palindrome("Good bye human."))
        self.assertFalse(is_palindrome("sunlight"))
        self.assertFalse(is_palindrome("Good morning everybody."))
        self.assertFalse(is_palindrome("casa"))
        self.assertFalse(is_palindrome("perro"))
        self.assertFalse(is_palindrome("Hola mundo."))
        self.assertFalse(is_palindrome("mariposa"))
        self.assertFalse(is_palindrome("Buenos días"))
        self.assertFalse(is_palindrome("oyasumi"))
    
# Los casos Edge no serían ejemplos de casi palíndromos que en realidad no lo son?
# No importa, lo dejo como en el ejemplo de GitHub.
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("XXX"))
        self.assertTrue(is_palindrome("zZZ"))
        self.assertTrue(is_palindrome("=="))
        self.assertTrue(is_palindrome("!!!"))
        self.assertTrue(is_palindrome("2002"))
        self.assertTrue(is_palindrome("Aa"))

if __name__ == '__main__':
    unittest.main()