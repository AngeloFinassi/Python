import pygame
pygame.init()

#Movimentação
def MoveCont(keys):
        if keys[pygame.K_LEFT]:
            rect_x -= move
            rect_x = max(0, rect_x)  # Limita o movimento para não sair da tela à esquerda
        elif keys[pygame.K_RIGHT]:
            rect_x += move
            rect_x = min(screen_width - rect_width, rect_x)  # Limita o movimento para não sair da tela à direita
        elif keys[pygame.K_DOWN]:
            rect_y += move
            rect_y = min(screen_height - rect_height, rect_y)  # Limita o movimento para não sair da tela abaixo
        elif keys[pygame.K_UP]:
            rect_y -= move
            rect_y = max(0, rect_y)  # Limita o movimento para não sair da tela acima

# Definição das dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Definição das dimensões do retângulo (snake)
rect_x = 0
rect_y = 0
rect_width = 20
rect_height = 20
move = 20

# Configuração do relógio
clock = pygame.time.Clock()
FPS = 15

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica do jogo
    keys = pygame.key.get_pressed()
    MoveCont(keys)

    # Renderização do jogo
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    clock.tick(FPS)

# Finalizando o Pygame
pygame.quit()
