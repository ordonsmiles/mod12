import unittest
import re
from datetime import datetime

def is_valid_symbol(symbol):
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))

def is_valid_chart_type(chart_type):
    return chart_type in {"1", "2"}

def is_valid_time_series(time_series):
    return time_series in {"1", "2", "3", "4"}

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):

    def test_valid_symbol(self):
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("GOOG"))
        self.assertTrue(is_valid_symbol("TSLA"))
        self.assertFalse(is_valid_symbol("AAPL123"))
        self.assertFalse(is_valid_symbol("aapl")) 
        self.assertFalse(is_valid_symbol("123"))

    def test_valid_chart_type(self):
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        self.assertFalse(is_valid_chart_type("3")) 
        self.assertFalse(is_valid_chart_type("A"))

    def test_valid_time_series(self):
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("2"))
        self.assertTrue(is_valid_time_series("3"))
        self.assertTrue(is_valid_time_series("4"))
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("A"))

    def test_valid_date(self):
        self.assertTrue(is_valid_date("2023-11-15"))
        self.assertTrue(is_valid_date("2000-01-01"))
        self.assertFalse(is_valid_date("2023/11/15"))
        self.assertFalse(is_valid_date("15-11-2023"))
        self.assertFalse(is_valid_date("2023-13-01"))
        self.assertFalse(is_valid_date("2023-11-32"))

if __name__ == "__main__":
    unittest.main()
