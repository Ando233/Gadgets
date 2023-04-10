def get_char_info(char):
    if char == 'e':
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 2],
                     [1, 2, 1, 2],
                     [1, 1, 2, 0],
                     [0, 1, 1, 2],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 'y':
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [1, 2, 0, 0],
                     [1, 2, 1, 2],
                     [1, 2, 1, 2],
                     [0, 1, 1, 2],
                     [0, 0, 1, 2],
                     [0, 0, 1, 2]]
    elif char == 'm':
        char_info = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 2, 0],
                     [1, 2, 1, 2, 1, 2],
                     [1, 2, 1, 2, 1, 2],
                     [1, 2, 1, 2, 1, 2],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
    elif char == 'u':
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [1, 2, 1, 2],
                     [1, 2, 1, 2],
                     [1, 2, 1, 2],
                     [0, 1, 2, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 's':
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 2],
                     [1, 2, 0, 0],
                     [0, 1, 1, 2],
                     [1, 1, 2, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 'l':
        char_info = [[1, 2, 0, 0],
                     [1, 2, 0, 0],
                     [1, 2, 0, 0],
                     [1, 2, 0, 0],
                     [1, 2, 1, 2],
                     [0, 1, 1, 2],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 'i':
        char_info = [[0, 1, 2, 0],
                     [0, 0, 0, 0],
                     [1, 1, 2, 0],
                     [0, 1, 2, 0],
                     [0, 1, 2, 0],
                     [0, 1, 1, 2],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == '>':
        char_info = [[0, 0, 0, 0],
                     [1, 2, 0, 0],
                     [0, 1, 2, 0],
                     [0, 0, 1, 2],
                     [0, 1, 2, 0],
                     [1, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 'a':
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 2],
                     [1, 2, 1, 2],
                     [1, 2, 1, 2],
                     [1, 1, 1, 2],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 't':
        char_info = [[0, 1, 2, 0],
                     [1, 1, 1, 2],
                     [0, 1, 2, 0],
                     [0, 1, 2, 0],
                     [0, 1, 2, 0],
                     [0, 1, 1, 2],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    elif char == 'r':
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 2],
                     [1, 2, 0, 0],
                     [1, 2, 0, 0],
                     [1, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    else:
        char_info = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 2],
                     [1, 2, 1, 2],
                     [1, 1, 2, 0],
                     [0, 1, 1, 2],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    return char_info