def print_pattern(rows, cols):
    pattern = [
      "X         X",
      "   X    X  ",
      "     X     ",
      "  X     X  ",
      "X         X"
    ]

    for i in range(rows):
        for line in pattern:
            print(line * cols)


print_pattern(5, 10)