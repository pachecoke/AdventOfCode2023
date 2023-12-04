import unittest
from day1 import main


class Day1Tests(unittest.TestCase):
    def test_get_first_digit_in_calibration(self):
        amended_calibration_value = "1abc2"
        calibration_value = main.get_first_digit(amended_calibration_value)
        self.assertEqual(calibration_value, 1)

    def test_get_last_digit_in_calibration(self):
        amended_calibration_value = "1abc2"
        calibration_value = main.get_last_digit(amended_calibration_value)
        self.assertEqual(calibration_value, 2)

    def test_recover_calibration_value(self):
        amended_calibration_value = "1abc2"
        calibration_value = main.recover_calibration_value(amended_calibration_value)
        self.assertEqual(calibration_value, 12)

    def test_recover_all_calibration_values(self):
        amended_calibration_values = "1abc2\n3def4\n5ghi6"
        calibration_values = main.recover_all_calibration_values(amended_calibration_values)
        self.assertEqual(calibration_values, [12, 34, 56])

    def test_sum_calibration_values(self):
        calibration_values = [12, 34, 56]
        sum = main.sum_calibration_values(calibration_values)
        self.assertEqual(sum, 102)
