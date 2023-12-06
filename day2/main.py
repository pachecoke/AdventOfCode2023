import sys


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def get_max_cubes(cubes_text):
    cubes = {"blue": 0, "red": 0, "green": 0}
    sets_text = cubes_text.split(";")  # ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
    for set_text in sets_text:
        colors_text = set_text.split(",")  # ["3 blue", "4 red"]
        for color_text in colors_text:
            color_text = color_text.strip()
            value, color = color_text.split(" ")
            if cubes[color] < int(value):
                cubes[color] = int(value)
    return cubes


def check_is_game_possible(cube_limits, cubes_text):
    cubes = get_max_cubes(cubes_text)
    for color, limit in cube_limits.items():
        if cubes[color] > limit:
            return False
    return True


def get_game_id(game_text):
    return int(game_text.split(" ")[1])


def solve_puzzle(input):
    possible_games = []
    for game_record in input.split("\n"):
        if game_record == "":
            continue
        game_text, cubes_text = game_record.split(":")
        cube_limits = {"blue": 14, "red": 12, "green": 13}
        if check_is_game_possible(cube_limits, cubes_text):
            possible_games.append(get_game_id(game_text))
    print(sum(possible_games))


if __name__ == "__main__":
    file_input = sys.argv[1]
    input = read_input(file_input)
    solve_puzzle(input)
