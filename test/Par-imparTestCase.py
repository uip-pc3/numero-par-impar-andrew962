import unittest
from App.main import num

class MyTestCase(unittest.TestCase):

    def test_impar(self):
        self.assertEquals(num(8),'Numero Par')