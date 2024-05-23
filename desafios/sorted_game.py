import random, pygame, sys, time

pygame.init()

def draw():
    screen.fill((0, 0, 0))
    for c in range(0, len(numbers)):
        n = numbers[c]
        pygame.draw.rect(screen, (255, 255, 255), (c* size, screen_height - n, size, n))

# Define as dimensões da janela
screen_widht, screen_height = 1920, 800
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption('Sorted Simulation')

#atualização da Tela
FPS = 60
clock = pygame.time.Clock()

#Vars
size = 10
times = 0.0001
numbers = []
temporary_size = screen_height

#numberList
for k in range(0, int(screen_widht / size)):
    temporary_size -= size
    numbers.append(temporary_size)
random.shuffle(numbers)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)

    length = len(numbers)
    for i in range(length):
        # range(0, n - i - 1) diminui a cada iteração do loop externo
        for k in range(0 , length - i - 1):
            draw()
            if numbers[k] > numbers[k + 1]:
                numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
                pygame.display.flip()
                time.sleep(times)
    break

    pygame.display.flip()
    