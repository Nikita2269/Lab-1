height = 9
width = 20

for y in range(height, -1, -1):
    row = ""
    for x in range(width + 1):
        if y == round(2 * x * height / width):
            row += "*"
        elif y == 0 and x == 0:
            row += "+"
        elif y == 0:
            row += "-"
        elif x == 0:
            row += "|"
        else:
            row += " "
    print(row)