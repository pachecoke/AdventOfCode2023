import unittest
from day2 import main


class Day2Tests(unittest.TestCase):
    def test_get_max_cubes(self):
        input = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        cubes = main.get_max_cubes(input)
        self.assertEqual(cubes, {"blue": 6, "red": 4, "green": 2})

    def test_check_is_game_possible(self):
        input = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        cube_limits = {"blue": 6, "red": 4, "green": 2}
        self.assertTrue(main.check_is_game_possible(cube_limits, input))
        cube_limits = {"blue": 6, "red": 4, "green": 1}
        self.assertFalse(main.check_is_game_possible(cube_limits, input))

    def test_get_game_id(self):
        input = "Game 1"
        self.assertEqual(main.get_game_id(input), 1)

    def test_calculate_cubes_power(self):
        cubes = {"blue": 6, "red": 4, "green": 2}
        set_power = main.calculate_cubes_power(cubes)
        self.assertEqual(set_power, 48)
