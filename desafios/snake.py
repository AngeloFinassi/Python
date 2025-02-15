import pygame
import random
pygame.init()      

#Movimentação
def LEFT():
    global rect_x
    rect_x -= move
    rect_x = max(0, rect_x)

def RIGHT():
    global rect_x
    rect_x += move
    rect_x = min(screen_width - rect_width, rect_x)

def DOWN():
    global rect_y
    rect_y += move
    rect_y = min(screen_height - rect_height, rect_y)

def UP():
    global rect_y
    rect_y -= move
    rect_y = max(0, rect_y)

#Funcionalidades
def div(num1, size):
    div = int((num1 / size)) * size
    return div


#Var Tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

#Var Snake
size = 20
rect_x = 0
rect_y = 0
rect_width = size
rect_height = size
move = 20

#Configuração do relógio
clock = pygame.time.Clock()
FPS = 20

#Var iniciais
running = True
move_left = True
move_up = False
case1 = False
case2 = False

# Posição inicial da maçã
apple_x = div(random.randint(0, (screen_width - size)), size)
apple_y = div(random.randint(0, (screen_height - size)), size)

#Texto
font = pygame.font.SysFont(None, 36)
score = 0

#Funcionalidade Corpo cobra
rect_body = list()
rect_body.append([rect_x, rect_y])

while running:
    print(rect_body)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Se apertar muda o estado das variaveis
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
                case1 = True
                case2 = False
            elif event.key == pygame.K_RIGHT:
                move_left = False
                case1 = True
                case2 = False
            elif event.key == pygame.K_UP:
                move_up = True
                case1 = False
                case2 = True
            elif event.key == pygame.K_DOWN:
                move_up = False
                case1 = False
                case2 = True

    #Dependendo do estado, chama certa função até mudar
    if case1:
        if move_left:
            LEFT()
        else:
            RIGHT()
    if case2:
        if move_up:
            UP()
        else:
            DOWN()
    
    #Renderização do jogo
    screen.fill((0, 0, 0))

    text_surface = font.render("Pontuação: " + str(score), True, (255, 255, 255))
    screen.blit(text_surface, (10, screen_height - 40))

    #Cobra
    for part in rect_body:
        pygame.draw.rect(screen, (255, 255, 255), (part[0], part[1], rect_width, rect_height))
    pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))

    #Desenhar a maçã
    pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, size, size))

    #Verificar colisão da cobra com a maçã
    if rect_x == apple_x and rect_y == apple_y:
        apple_x = div(random.randint(0, (screen_width - size)), size)
        apple_y = div(random.randint(0, (screen_height - size)), size)
        rect_body.append([rect_x, rect_y])
        score += 1

    #Cria lista para cada nova parte do corpo
    for c in (rect_x, rect_y):
        rect_body[score][0] = rect_x
        rect_body[score][1] = rect_y

    #Atualiza cordenadas de cada parte do corpo, dps a da cabeça
    for i in range(len(rect_body) -1, 0, -1):
        rect_body[i] = rect_body[i - 1]
    rect_body[0] = [rect_x, rect_y]

    #Mecanismo de perder, caso a cabeça encoste em alguma parte do corpo
    '''for part in rect_body[1:]:
        if part[0] == rect_x and part[1] == rect_y:
            running = False'''

    pygame.display.flip()
    clock.tick(FPS)

# Finalizando o Pygame
pygame.quit()
