import unittest
from numbers import Numbers

class NumbersTestCase(unittest.TestCase):
    def setUp(self):
        self.number = Numbers()

    def test_init_number(self):
        self.assertEqual(self.number.num, 13, msg = "Invalid Number")

    
    def test_retrn_error_if_number_is_str(self):
        self.assertRaises(ValueError, self.number.__init__, 'two')
 
    def test_return_error_if_number_is_float(self):
        self.assertRaises(ValueError, self.number.__init__, 2.3)
    
    def test_fuzzbuzz_exists(self):
        fuzz = self.number.fuzzbuzz()
        self.assertTrue(fuzz is not None)

    def test_fibinacci_exists(self):
        fibo = self.number.fibonacci()
        self.assertTrue(fibo is not None)

    
    def test_factoorial_exists(self):
        facto = self.number.factorial()
        self.assertTrue(facto is not None)