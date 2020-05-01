import pandas as pd
from configparser import ConfigParser
import tableauserverclient as TSC
import psycopg2
from pandas.util.testing import assert_frame_equal
from parameterized import parameterized
import unittest


class SimpleTest(unittest.TestCase):

    @parameterized.expand([
        [1],
        [2],
        [3],
    ])
    def test_validation(self, key):
        self.assertTrue(True)

    def test_frame(self):
        df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
        assert_frame_equal(df1, df2, check_dtype=False)


if __name__ == '__main__':
    unittest.main()
