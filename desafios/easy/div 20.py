import random
screen_width = 800
screen_height = 600
size = 20

def div(num1, num2, size):
    div1 = int((num1 / size)) * size
    div2 = int((num2 /size)) * size
    return div1, div2

apple_x = random.randint(0, (screen_width - size))
apple_y = random.randint(0, (screen_height - size))
print(div(apple_x, apple_y, size))