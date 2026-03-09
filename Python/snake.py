import pygame
from time import sleep
from random import randint

pygame.init()

screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption("Snake Game")
running = True
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()

# x, y cua moi con ran
# tail - head
snakes = [[5, 10]]

direction = "up"

apple = [randint(0, 19), randint(0, 19)]

font_small = pygame.font.SysFont("comicsansms", 20)
font_big = pygame.font.SysFont("comicsansms", 50) 

score = 0

pausing = False

while running:
    clock.tick(10)
    screen.fill(BLACK)
    
    tail_x = snakes[0][0]
    tail_y = snakes[0][1]
    
    # Draw Grid
    # for i in range(21):
    #     pygame.draw.line(screen, WHITE, (0, i*30), (600, i*30))
    #     pygame.draw.line(screen, WHITE, (i*30, 0), (i*30, 600))

    # Draw Snake
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))
    
    # Draw Apple
    pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    # Point
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0, [tail_x, tail_y])
        
        # Make sure apple not in snake
        while apple in snakes:
            apple = [randint(0, 19), randint(0, 19)]

        score += 1

    # Check crash with edge
    if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
        pausing = True 

    # Draw Score
    score_txt = font_small.render("Score: " + str(score), True, WHITE)
    screen.blit(score_txt, (5,5))

    # Snake Move
    if pausing == False:
        if direction == "right":
            snakes.append([snakes[-1][0]+1, snakes[-1][1]])
            snakes.pop(0)
        elif direction == "left":   
            snakes.append([snakes[-1][0]-1, snakes[-1][1]])
            snakes.pop(0)
        elif direction == "up":
            snakes.append([snakes[-1][0], snakes[-1][1]-1])
            snakes.pop(0)
        elif direction == "down":
            snakes.append([snakes[-1][0], snakes[-1][1]+1])
            snakes.pop(0)

    # Check crash with body
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
            pausing = True

    # Draw game over
    if pausing:
        game_over_txt = font_big.render("Game Over, Score:" + str(score), True, WHITE)
        press_space_txt = font_big.render("Press Space to continue", True, WHITE)
        screen.blit(game_over_txt, (50, 200))
        screen.blit(press_space_txt, (50, 300))   

    sleep(0.05)    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "down":
                direction = "up"
            if event.key == pygame.K_s and direction != "up":
                direction = "down"
            if event.key == pygame.K_a and direction != "right":
                direction = "left"
            if event.key == pygame.K_d and direction != "left":
                direction = "right"
            if event.key == pygame.K_SPACE and pausing == True:
                pausing = False
                snakes = [[5, 10]]
                apple = [randint(0, 19), randint(0, 19)]
                score = 0 


    pygame.display.flip()

pygame.quit()
