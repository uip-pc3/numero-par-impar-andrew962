import unittest
from App.main import num

class MyTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.num=num(9)

    #def test_par(self):
     #   self.assertNotEqual(self.num,0,'Incorrecto')

    def test_impar(self):
        self.assertEquals(num(9),'Numero Impar')