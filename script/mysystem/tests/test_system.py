import unittest

from .. import mysystem

class TestPlatform(unittest.TestCase):

    def test_system(self):
        self.assertTrue(mysystem.is_supported_os('Linux'))
        self.assertFalse(mysystem.is_supported_os('Windows'))

    def test_memory(self):
        for mem in [ 64, 128, 256 ]: 
            self.assertTrue(mysystem.is_enough_memory(mem))

        for mem in [ 16 , 24 , 32, 65, 'A' ]: 
            self.assertFalse(mysystem.is_enough_memory(mem))

if __name__ == "__main__":
    unittest.main()

