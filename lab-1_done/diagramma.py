import math

with open('sequence.txt', 'r') as file:
    sequence = [float(line.strip()) for line in file]

even_positions = sequence[::2]
odd_positions = sequence[1::2]

even_sum = sum(abs(num) for num in even_positions)
odd_sum = sum(abs(num) for num in odd_positions)

total_sum = even_sum + odd_sum
even_percentage = (even_sum / total_sum) * 100
odd_percentage = (odd_sum / total_sum) * 100

def draw_pie_chart(even_percentage, odd_percentage):
    radius = 10
    diameter = radius * 2
    chart = [[' ' for _ in range(diameter)] for _ in range(diameter)]
    cx, cy = radius, radius

    for y in range(diameter):
        for x in range(diameter):
            distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)

            if distance < radius:
                angle = math.degrees(math.atan2(y - cy, x - cx))
                if angle < 0:
                    angle += 360

                if angle < even_percentage * 360 / 100:
                    chart[y][x] = '#'
                elif angle < (even_percentage + odd_percentage) * 360 / 100:
                    chart[y][x] = '*'

    for row in chart:
        print(''.join(row))
        
print("Процентное соотношение суммы чисел по модулю:")
print(f'Чётные позиции: {even_percentage:.2f}%')
print(f'Нечётные позиции: {odd_percentage:.2f}%')

draw_pie_chart(even_percentage, odd_percentage)