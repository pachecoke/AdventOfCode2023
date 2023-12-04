import sys


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def get_first_digit(amended_calibration_value):
    for character in amended_calibration_value:
        if character.isdigit():
            first = int(character)
            return first
    raise Exception(f"No digits found in the input: {amended_calibration_value}")


def get_last_digit(amended_calibration_value):
    for character in reversed(amended_calibration_value):
        if character.isdigit():
            last = int(character)
            return last
    raise Exception(f"No digits found in the input: {amended_calibration_value}")


def recover_calibration_value(amended_calibration_value):
    first = get_first_digit(amended_calibration_value)
    last = get_last_digit(amended_calibration_value)
    return int(f"{first}{last}")


def recover_all_calibration_values(amended_calibration_values):
    calibration_values = []
    for amended_calibration_value in amended_calibration_values.split("\n"):
        if amended_calibration_value == "":
            continue
        calibration_value = recover_calibration_value(amended_calibration_value)
        calibration_values.append(calibration_value)
    return calibration_values


def sum_calibration_values(calibration_values):
    return sum(calibration_values)


def solve_puzzle_part_1(input):
    calibration_values = recover_all_calibration_values(input)
    sum = sum_calibration_values(calibration_values)
    print(sum)


if __name__ == "__main__":
    file_input = sys.argv[1]
    input = read_input(file_input)
    solve_puzzle_part_1(input)
