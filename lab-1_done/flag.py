RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

print(f"{RED}{" "*10}{END}")
print(f"{WHITE}{" "*10}{END}")
print(f"{BLUE}{" "*10}{END}")


'''
def draw_line(offset=0, length=1, color=41):
    line = " " * length
    print(f"{' ' * offset}\u001b[{color}m{line}{END}")


draw_line(0, 10, 41)
draw_line(0, 10, 47)
draw_line(0, 10, 44)
'''