'''
Checks if game board solution is correct
Github repository:
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    file = open(path, mode='r', encoding='utf-8').readlines()
    lines = [w.strip() for w in file]
    return lines



def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    >>> left_to_right_check("132354*", 3)

    """
    row = input_line[1:6]
    visible = [1]
    base = int(row[0])
    for i in range(len(row)-1):
        if base < int(row[i+1]):
            visible.append(1)
            base = int(row[i])

    if len(visible) == pivot:
        return True
    return False


def right_to_left_check(input_line, pivot):
    """
    Check row-wise visibility from right to left.
    Return True if number of building from the right-most hint is visible looking to the left,
    False otherwise.

    input_line - representing board row.
    pivot - number on the right-most hint of the input_line.

    >>> right_to_left_check("*543215", 5)
    True
    >>> right_to_left_check("452453*", 5)
    False
    """
    return left_to_right_check(input_line[::-1], pivot)


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        for hint in row:
            if hint == '?':
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board[1:6]:
        hints = row[1:6]
        for hint in hints:
            rep = hints.count(hint)
            if rep > 1:
                return False
    return True