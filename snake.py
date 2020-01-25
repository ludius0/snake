import pygame, random
from pygame.locals import *

display = 600
rows = 20
score = 0

def on_grid_random():
    x = random.randrange(0, display, rows)
    y = random.randrange(0, display, rows)
    return (x, y)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def move(dirnx, dirny):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                
    keys = pygame.key.get_pressed()

    for key in keys:
        if keys[pygame.K_LEFT]:
            dirnx = -1
            dirny = 0
        elif keys[pygame.K_RIGHT]:
            dirnx = 1
            dirny = 0
        elif keys[pygame.K_UP]:
            dirny = -1
            dirnx = 0
        elif keys[pygame.K_DOWN]:
            dirny = 1
            dirnx = 0
    return dirnx, dirny

def grid(screen):   # Generate a grip in form of cubes
    x, y = 0, 0

    for x in range(0, display, rows): # Draw vertical lines
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, display))
    for y in range(0, display, rows): # Draw vertical lines
            pygame.draw.line(screen, (40, 40, 40), (0, y), (display, y))


def main():
    global apple_pos, score
    pygame.init()
    screen = pygame.display.set_mode((display, display))
    pygame.display.set_caption('Snake')

    snake = [(200, 200)]
    snake_skin = pygame.Surface((rows, rows))
    snake_skin.fill((255,255,255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((rows, rows))
    apple.fill((255,0,0))

    clock = pygame.time.Clock()
    game = True
    dirnx = 0
    dirny = 1
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    score = 0
    while game:
        clock.tick(15)

        dirnx, dirny = move(dirnx, dirny)
                        
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            score += 1

         # Check if snake collided with boundaries
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
            game = False
            break
        
        # Check if the snake has hit itself
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game = False
                break
            
        if game == False:
            break

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        if dirnx == -1 and dirny == 0:
            snake[0] = (snake[0][0] - rows, snake[0][1])
        elif dirnx == 1 and dirny == 0:
            snake[0] = (snake[0][0] + rows, snake[0][1])
        elif dirnx == 0 and dirny == -1:
            snake[0] = (snake[0][0], snake[0][1] - rows)
        elif dirnx == 0 and dirny == 1:
            snake[0] = (snake[0][0], snake[0][1] + rows)

        screen.fill((60, 150, 100))
        screen.blit(apple, apple_pos)
        grid(screen)

        pygame.display.flip()
        for pos in snake:
            screen.blit(snake_skin,pos)

        pygame.display.update()


if __name__ == "__main__":
    main()
    print(f"You ate {score} an apples!")
