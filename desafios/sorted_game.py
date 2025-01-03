import random, pygame, sys, time

pygame.init()

def draw():
    screen.fill((0, 0, 0))
    for c in range(0, len(numbers)):
        n = numbers[c]
        pygame.draw.rect(screen, (255, 255, 255), (c* size, screen_height - n, size, n))

def bubble():
    length = len(numbers)
    for i in range(length):
        # range(0, n - i - 1) diminui a cada iteração do loop externo
        for k in range(0 , length - i - 1):
            draw()
            if numbers[k] > numbers[k + 1]:
                numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
            pygame.display.flip()
            time.sleep(times)
        

def selection(numbers):
    for i in range(len(numbers)):
        min_index = i
        for k in range(1 + i, len(numbers)):
            draw()
            if numbers[k] < numbers[min_index]:
                min_index = k     
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
        pygame.display.flip()
        time.sleep(times)
        

# Define as dimensões da janela
screen_widht, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption('Sorted Simulation')

#atualização da Tela
FPS = 120
clock = pygame.time.Clock()

#Vars
size = 20
times = 0
numbers = []
temporary_size = screen_height

#numberList
numbers = [
    screen_height - size * k 
    for k in range(int(screen_widht / size)) 
    if screen_height - size * k > 0
]
random.shuffle(numbers)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)

    #bubble(numbers)
    selection(numbers)
    print(numbers)
    time.sleep(3)
    break