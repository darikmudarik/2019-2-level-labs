"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if type(num_rows) != int or type(num_cols) != int:
        return []
    matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]
    return matrix

def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    edit_matrix = list(edit_matrix)
    if type(add_weight) != int or type(remove_weight) != int:
        return edit_matrix
    if not edit_matrix or not edit_matrix[0]:
        return edit_matrix
    for i in range(1, len(edit_matrix)):
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
    for j in range(1, len(edit_matrix[0])):
        edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
    return edit_matrix

def minimum_value(numbers: tuple) -> int:
    numbers = list(numbers)
    min_number = min(numbers)
    return min_number

def fill_edit_matrix(edit_matrix: tuple,
                    add_weight: int,
                    remove_weight: int,
                    substitute_weight: int,
                    original_word: str,
                    target_word: str) -> list:
    matrix = list(edit_matrix)
    if type(add_weight) != int or type(remove_weight) != int or type(substitute_weight) != int:
        return matrix
    if type(original_word) != str or type(target_word) != str:
        return matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            add = matrix[i][j - 1] + add_weight
            remove = matrix[i - 1][j] + remove_weight
            if original_word[i - 1] == target_word[j - 1]:
                substitute = matrix[i - 1][j - 1]
            else:
                substitute = matrix[i - 1][j - 1] + substitute_weight
            matrix[i][j] = minimum_value((add, remove, substitute))
    return matrix

def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if type(original_word) != str or type(target_word) != str:
        return -1
    if type(add_weight) != int or type(remove_weight) != int or type(substitute_weight) != int:
        return -1
    matrix = tuple(generate_edit_matrix(len(original_word) + 1, len(target_word) + 1))
    matrix = initialize_edit_matrix(matrix, add_weight, remove_weight)
    matrix = fill_edit_matrix(tuple(matrix), add_weight, remove_weight, substitute_weight)
    distance = matrix[-1][-1]
    return distance

def load_from_csv(path_to_file: str) -> list:
    with open(path_to_file) as file:
        matrix = []
        data = file.read().split('\n')
        if '' in data:
            data.remove('')
        for row in data:
            matrix.append(row.split(','))
    return matrix

def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    with open(path_to_file, 'w') as file:
        for row in edit_matrix:
            line = ''
            for column in row:
                line += (str(column) + ',')
            file.write(line[:-1] + '\n')
