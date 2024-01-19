def binary_to_move(bin_code, is_binary=True):
    if not is_binary:
        bin_code = bin(bin_code)[2:]

    direction_map = {
        "將": {"00": "前", "01": "右", "10": "後", "11": "左"},
        "士": {"00": "右上", "01": "右下", "10": "左下", "11": "左上"},
        "馬": {"000": "1點鐘方向", "001": "2點鐘方向", "010": "4點鐘方向", "011": "5點鐘方向",
              "100": "7點鐘方向", "101": "8點鐘方向", "110": "10點鐘方向", "111": "11點鐘方向"},
        "卒": {"00": "前", "01": "右", "10": "左"},
        "象": {"00": "右上", "01": "右下", "10": "左下", "11": "左上"},
        "車": {
            "0000": "往右1", "0001": "往右2", "0010": "往右3", "0011": "往右4",
            "0100": "往右5", "0101": "往右6", "0110": "往右7", "0111": "往右8",
            "1000": "往前1", "1001": "往前2", "1010": "往前3", "1011": "往前4",
            "1100": "往前5", "1101": "往前6", "1110": "往前7", "1111": "往前8",
        },
        "炮": {
            "0000": "往右1", "0001": "往右2", "0010": "往右3", "0011": "往右4",
            "0100": "往右5", "0101": "往右6", "0110": "往右7", "0111": "往右8",
            "1000": "往前1", "1001": "往前2", "1010": "往前3", "1011": "往前4",
            "1100": "往前5", "1101": "往前6", "1110": "往前7", "1111": "往前8",
        }
    }

    piece_map = {
        "將": (3, "0"), "士": (3, "0"), "馬": (4, "0"),
        "卒": (5, "010"), "象": (5, "000"),
        "車": (6, "00"), "炮": (6, "10"),
    }

    piece_index_map = {
        "0": "第一個", "1": "第二個",
        "00": "第一個", "01": "第二個",
        "10": "第一個", "11": "第二個",
        "000": "第一個", "001": "第二個",
        "010": "第一個", "011": "第二個", "100": "第三個", "101": "第四個", "110": "第五個"
    }

    if len(bin_code) == 2:
        piece = "車" if bin_code[0] == "0" else "炮"
        piece_name = piece_index_map[bin_code] + piece
        return f"{piece_name}往前9"

    for piece, (length, prefix) in piece_map.items():
        if len(bin_code) == length and bin_code.startswith(prefix):
            piece_index = bin_code[:len(prefix)]
            direction_bits = bin_code[len(prefix):]
            move = direction_map[piece].get(direction_bits, "Invalid move")
            if move != "Invalid move":
                piece_name = piece_index_map[piece_index] + piece
                return f"{piece_name}{move}"

    return "Invalid input"


# 將:1 士:2 象:3 車:4 馬:5 炮:6 卒:7
# 第一隻馬的第三種走步
# move_to_binary(5, 1, 3) -> 0010
def move_to_binary(piece, num, direction):
    piece_binary_map = {
        1: "0",   # 將
        2: "1",   # 士
        3: {1: "000", 2: "001"},   # 象
        4: {1: "00", 2: "01"},     # 車
        5: {1: "0", 2: "1"},       # 馬
        6: {1: "10", 2: "11"},     # 炮
        7: {1: "010", 2: "011", 3: "100", 4: "101", 5: "110"}  # 卒
    }

    direction_map = {
        1: {1: "00", 2: "01", 3: "10", 4: "11"},
        2: {1: "00", 2: "01", 3: "10", 4: "11"},
        3: {1: "00", 2: "01", 3: "10", 4: "11"},
        4: {1: "0000", 2: "0001", 3: "0010", 4: "0011",
            5: "0100", 6: "0101", 7: "0110", 8: "0111",
            9: "1000", 10: "1001", 11: "1010", 12: "1011",
            13: "1100", 14: "1101", 15: "1110", 16: "1111"},
        5: {1: "000", 2: "001", 3: "010", 4: "011",
            5: "100", 6: "101", 7: "110", 8: "111"},
        6: {1: "0000", 2: "0001", 3: "0010", 4: "0011",
            5: "0100", 6: "0101", 7: "0110", 8: "0111",
            9: "1000", 10: "1001", 11: "1010", 12: "1011",
            13: "1100", 14: "1101", 15: "1110", 16: "1111"},
        7: {1: "00", 2: "01", 3: "10"}
    }

    piece_binary = piece_binary_map[piece][num] if piece not in [
        1, 2] else piece_binary_map[piece]
    direction_binary = direction_map[piece][direction]
    binary_code = piece_binary + direction_binary

    return binary_code


def print_board(board_array):
    chinese_numbers = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    size = len(board_array)
    row_numbers = chinese_numbers[:size]

    print('  ', end='  ')
    for i in range(1, size):
        print(i, end='  ')
    print()

    for i, line in enumerate(board_array):
        print(row_numbers[i], end=' ')
        for value in line:
            c = value if value != '.' else '  '
            print(c, end=' ')
        print()
    print()


board_example = [
    ['車', '馬', '象', '士', '將', '士', '象', '馬', '車'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '炮', '.', '.', '.', '.', '.', '炮', '.'],
    ['卒', '.', '卒', '.', '卒', '.', '卒', '.', '卒'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['兵', '.', '兵', '.', '兵', '.', '兵', '.', '兵'],
    ['.', '炮', '.', '.', '.', '.', '.', '炮', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['車', '馬', '象', '士', '帥', '士', '象', '馬', '車']
]

print_board(board_example)
print(move_to_binary(5, 1, 3))  # -> 0010

example_1 = binary_to_move("000001", is_binary=True)  # 第一個車往右2
example_2 = binary_to_move("10", is_binary=True)  # 第一個炮 第17種走法

print(example_1, example_2)
