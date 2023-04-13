# tests.py

import xmlrunner
import unittest

class SimpleTest(unittest.TestCase):
    
    def test_pass1(self):
        self.assertEqual(10, 7 + 3)

    def test_pass2(self):
        self.assertTrue(True)

    def test_fail1(self):
        self.assertEqual(11, 7 + 4)

    def test_fail1(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))