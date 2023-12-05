import sys
import re


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def get_first_calibration_value(amended_calibration_value):
    digit_value, digit_index = get_first_digit(amended_calibration_value)
    word_value, word_index = get_first_number_word(amended_calibration_value)
    if digit_index != -1 and digit_index < word_index:
        return digit_value
    return word_to_digit[word_value]


def get_last_calibration_value(amended_calibration_value):
    digit_value, digit_index = get_last_digit(amended_calibration_value)
    word_value, word_index = get_last_number_word(amended_calibration_value)
    if digit_index > word_index:
        return digit_value
    return word_to_digit[word_value]


def get_first_digit(amended_calibration_value):
    for character in amended_calibration_value:
        if character.isdigit():
            first = int(character)
            return first, amended_calibration_value.find(str(first))
    return "", -1


def get_last_digit(amended_calibration_value):
    for character in reversed(amended_calibration_value):
        if character.isdigit():
            last = int(character)
            return last, amended_calibration_value.rfind(str(last))
    return "", -1


def recover_calibration_value(amended_calibration_value):
    first = get_first_calibration_value(amended_calibration_value)
    last = get_last_calibration_value(amended_calibration_value)
    return int(f"{first}{last}")


def recover_all_calibration_values(amended_calibration_values):
    calibration_values = []
    i = 0
    for amended_calibration_value in amended_calibration_values.split("\n"):
        i = i + 1
        if amended_calibration_value == "":
            continue
        calibration_value = recover_calibration_value(amended_calibration_value)
        calibration_values.append(calibration_value)
    return calibration_values


def sum_calibration_values(calibration_values):
    return sum(calibration_values)


word_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_indices_of_word(word, input):
    return [m.start() for m in re.finditer(word, input)]


def get_indices_of_words(input):
    indices = {}
    for word in word_to_digit:
        word_indices = get_indices_of_word(word, input)
        if word_indices != []:
            indices[word] = word_indices
    return indices


def get_first_number_word(input):
    indices = get_indices_of_words(input)
    smallest_index = sys.maxsize
    smallest_word = None
    for word in indices:
        word_indices = indices[word]
        if min(word_indices) < smallest_index:
            smallest_index = min(word_indices)
            smallest_word = word
    return smallest_word, smallest_index


def get_last_number_word(input):
    indices = get_indices_of_words(input)
    largest_index = -1
    largest_word = None
    for word in indices:
        word_indices = indices[word]
        if max(word_indices) > largest_index:
            largest_index = max(word_indices)
            largest_word = word
    return largest_word, largest_index


def solve_puzzle(input):
    calibration_values = recover_all_calibration_values(input)
    sum = sum_calibration_values(calibration_values)
    print(sum)


if __name__ == "__main__":
    file_input = sys.argv[1]
    input = read_input(file_input)
    solve_puzzle(input)
