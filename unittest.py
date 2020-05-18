import unittest
from Arene import *


class TestArene(unittest.TestCase):

    def test_generer(self):
        arene=Arene('areneTest')
        structureArene=arene.generer()
        self.assertEqual(structureArene,[1,0])        
        
        





"""class TestCapteur(unittest.TestCase):

    def test_murD:"""
        

if __name__=='__main__':
    unittest.main()
