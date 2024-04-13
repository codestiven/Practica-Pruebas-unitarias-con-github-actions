import unittest
import sys
import os

# Obtener la ruta al directorio padre de la carpeta 'test' (donde se encuentra 'test_app.py')
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

# Agregar la ruta al directorio que contiene 'app.py' al PYTHONPATH
sys.path.append(parent_dir)

# Importar 'app' desde 'app.py'
from app import app

# Resto del código de prueba

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '¡Hola, mundo!')

if __name__ == '__main__':
    unittest.main()
