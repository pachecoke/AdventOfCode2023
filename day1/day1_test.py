import unittest
from day1 import main


class Day1Tests(unittest.TestCase):
    def test_get_first_digit_in_calibration1(self):
        amended_calibration_value = "1abc2"
        calibration_value, index = main.get_first_digit(amended_calibration_value)
        self.assertEqual(calibration_value, 1)
        self.assertEqual(index, 0)

    def test_get_first_calibration_value_when_digit(self):
        amended_calibration_value = "z3oneight234"
        calibration_value = main.get_first_calibration_value(amended_calibration_value)
        self.assertEqual(calibration_value, 3)

    def test_get_first_calibration_value_when_word(self):
        amended_calibration_value = "zoneight234"
        calibration_value = main.get_first_calibration_value(amended_calibration_value)
        self.assertEqual(calibration_value, 1)

    def test_get_last_calibration_value_when_digit(self):
        amended_calibration_value = "zoneight234"
        calibration_value = main.get_first_calibration_value(amended_calibration_value)
        self.assertEqual(calibration_value, 1)

    def test_get_last_calibration_value_when_word(self):
        amended_calibration_value = "zoneight234nine"
        calibration_value = main.get_last_calibration_value(amended_calibration_value)
        self.assertEqual(calibration_value, 9)

    def test_get_last_digit_in_calibration(self):
        amended_calibration_value = "1abc2"
        calibration_value, index = main.get_last_digit(amended_calibration_value)
        self.assertEqual(calibration_value, 2)
        self.assertEqual(index, 4)

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

    def test_get_first_number_word(self):
        input = "zoneight234"
        first_number_word, index = main.get_first_number_word(input)
        self.assertEqual(first_number_word, "one")
        self.assertEqual(index, 1)

    def test_get_last_number_word(self):
        input = "zoneight234two"
        last_number_word, index = main.get_last_number_word(input)
        self.assertEqual(last_number_word, "two")
        self.assertEqual(index, 11)

    def test_get_index_of_word(self):
        input = "ztwoight234two"
        indices = main.get_indices_of_word("two", input)
        self.assertEqual(indices, [1, 11])
