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

if __name__ == '__main__':
    unittest.main()