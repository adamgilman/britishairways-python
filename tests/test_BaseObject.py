import unittest

from britishair import BA

class TestBAObject(unittest.TestCase):
    def setUp(self):
        self.ba = BA()

    def test_BAObject(self):
        self.assertTrue( type(self.ba) is BA )