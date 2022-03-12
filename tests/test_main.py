import unittest
from main import main

class MainTestCase(unittest.TestCase):
    
    def test_main(self):
        '''Test de prueba para main'''
        self.assertTrue(main())
        
    def test_saludo(self):
        '''Test de prueba para saludo'''
        self.assertEqual(main('saludar'), 'Hola mundo')
    
    def test_despedida(self):
        '''Test de prueba para despedida'''
        self.assertEqual(main('despedir'), 'Adiosss')