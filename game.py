import pygame
import math
import random

display = 600
rows = 15

class snake():

    def move():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                print("Left")
            elif keys[pygame.K_RIGHT]:
                print("Right")
            elif keys[pygame.K_UP]:
                print("Up")
            elif keys[pygame.K_DOWN]:
                print("Down")
                         
        redrawScreen()



def redrawScreen():
    global screen
    background.fill((60, 150, 100))
    
    grid(display, rows, background)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()


def grid(d, rows, background):
    position = d // rows
    x = 0
    y = 0
    # draw 20 times for x and y line
    for l in range(rows):
        x += position
        y += position
        pygame.draw.line(background, (0, 0, 0), (x,0),(x,d))
        pygame.draw.line(background, (0, 0, 0), (0,y),(d,y))


def apple(d, screen):
    x = random.randrange(0, d, rows)
    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 100, 100))


def main():
    global screen, background
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((display, display))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    

    

    while 1:
        pygame.time.delay(40)
        clock.tick(40)

        apple(display, background)

        snake.move()
#        redrawScreen()


if __name__ == "__main__": main()
