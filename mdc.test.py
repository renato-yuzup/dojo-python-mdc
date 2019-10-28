import unittest
from mdc import *

class TestMDC(unittest.TestCase):
    def testTrivialCase(self):
        mdc = MDC()
        self.assertEqual(mdc.calcMDC(1, 1), 1)

    def testMDCWithTwoSmallNumbers(self):
        mdc = MDC()
        self.assertEqual(mdc.calcMDC(1, 2), 1)

    def testMDCWithThreeSmallNumbers(self):
        mdc = MDC()
        self.assertEqual(mdc.calcMDC(1, 5, 1), 1)

    def testMDCWithTwoNumbers(self):
        mdc = MDC()
        self.assertEqual(mdc.calcMDC(2, 2), 2)


if __name__ == '__main__':
    unittest.main()
