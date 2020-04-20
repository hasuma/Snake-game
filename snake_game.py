import random
import pygame
from pygame.locals import *
#FUNCAO PARA DEFINIR POSICAO ALEATORIA DA APPLE DENTRO DO GRID
def on_grid_random():
    x = random.randint(1,60)
    y = random.randint(6,65)
    return (x * 10, y * 10)

#FUNCAO QUE DEFINE A COLISAO ENTRE SNAKE E A APPLE
def collision(c1,c2):
    return(c1[0] == c2[0] and c1[1]==c2[1]) #POSICAO (X,Y) DA APPLE E DA CABECA DA SNAKE IGUAL

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
#CONFIG SCREEN
screen = pygame.display.set_mode((620,670))
pygame.display.set_caption('Snake GAME')
screen_skin = pygame.Surface((10,10))
screen_skin.fill((255,255,255)) #RGB - BRANCO


#CONFIG - SNAKE
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0)) #RGB - VERDE

#CONFIG - APPLE
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #RGB - VERMELHO
apple_pos = on_grid_random()

#DIRECAO INICIAL
my_direction = LEFT

#LIMITANDO CLOCK
clock = pygame.time.Clock()

#CONFIG - SCORE
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

fast = 10
game_over = False
while not game_over:
    if score != 0 and score%10 == 0:
        fast += 5

    clock.tick(fast)

    #EVENTOS
    for event in pygame.event.get():
        if event.type == QUIT:  #SAIR FECHANDO TELA
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:  # SAIR TECLA 'Q'
                pygame.quit()
                exit()
            if event.key == K_UP and my_direction != DOWN:   #UP
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP: #DOWN
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:    #RIGHT
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:     #LEFT
                my_direction = LEFT

    #DEFININDO COLISOES
    if collision(snake[0],apple_pos):   #SNAKE - APPLE
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
    if snake[0][0] < 10:    #SNAKE - PAREDE ESQUERDA
        game_over = True
        break
    if snake[0][0] >= 610:    #SNAKE - PAREDE DIREITA
        game_over = True
        break
    if snake[0][1] < 60:    #SNAKE - PAREDE SUPERIOR
        game_over = True
        break
    if snake[0][1] >= 660:    #SNAKE - PAREDE INFERIOR
        game_over = True
        break

    #SNAKE - SNAKE
    for i in range(1,len(snake)-1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    # DEFININDO MOVIMENTO
    for i in range(len(snake) - 1, 0, -1):  # PERCORRENDO CADA POSICAO DO CORPO DA SNAKE DE TRAS PARA FRENTE
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    #DEFININDO DIRECOES PARA MOVIMENTO
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    #LIMPANDO TELA
    screen.fill((0,0,0))

    #BORDA SCREEN
    for pos in range(0, 611, 10):
        screen.blit(screen_skin, (pos, 50))
        screen.blit(screen_skin, (pos, 660))
        screen.blit(screen_skin, (0, pos+50))
        screen.blit(screen_skin, (610, pos+50))

    #GRID
    for x in range(0, 620, 10):  #LINHAS HORIZONTAIS
        pygame.draw.line(screen, (40, 40, 40), (x, 50), (x, 670))
    for y in range(0, 620, 10):  #LINHAS VERTICAIS
        pygame.draw.line(screen, (40, 40, 40), (0, y+50), (620, y+50))

    #SCORE
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (10, 10)
    screen.blit(score_font, score_rect)

    #BLIT: FUNCAO PARA PLOTAR NO SCREEN
    screen.blit(apple, apple_pos)      #PLOTANDO APPLE EM POSICAO ALEATORIA
    for pos in snake:
        screen.blit(snake_skin, pos)    #PLOTANDO SNAKE

    pygame.display.update()


while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 40)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255,255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (310, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

