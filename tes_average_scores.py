"""
program: tes_average_.py
Author: Ondrea
Last date modfied: 06/07/20

The purpose of this program is to test average_scores.py
"""

import unittest
import unittest.mock as mock
from format_output import average_scores as avg

class MyTestCase(unittest.TestCase):
#my class definitions
    def test_average(self):
    with mock.patch('builtins.input', side_effect=[85,90,95]):
        assert topic2.average() == 90



if __name__ == '__main__':
    unittest.main()

#The program ran in 0.001s
#Test ran OK
#Observed output: average: 90.0
