import pygame, math, random
from pygame.locals import *

display = 600
rows = 20
d = display
apple_pos_list = [0, 0, 0, 0, False]


class snake():

    def draw_snake(display, body):
        position = display // rows
        a, b = 0, 0
        a += position
        b += position
        pygame.draw.rect(background, (0, 100, 255), (body[0], body[1], a, b))

    def move(display, snake_direction, body):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                snake_direction = "LEFT"
                print("Left")
            elif keys[pygame.K_RIGHT]:
                snake_direction = "RIGHT"
                print("Right")
            elif keys[pygame.K_UP]:
                snake_direction = "UP"
                print("Up")
            elif keys[pygame.K_DOWN]:
                snake_direction = "DOWN"
                print("Down")


        position = display // rows
        x, y = 0, 0
        x += position
        y += position
        

        if body[0] <= 0:
            body[0] = 0 
        if body[1] <= 0:
            body[1] = 0 

        if snake_direction == "LEFT":
            body[0] = body[0] - x
        elif snake_direction == "RIGHT":
            body[0] = body[0] + x
        elif snake_direction == "UP":
            body[1] = body[1] - y
        elif snake_direction == "DOWN":
            body[1] = body[1] + y


        snake.draw_snake(display, body)
                         
        redraw_screen(background)

    def collision_apple():
        snack = False

    def collision_snake():
        pass



def redraw_screen(background):
    background.fill((60, 150, 100))
    
    grid(display, rows, background)
    apple(display, background)
    
    screen.blit(background, (0, 0))
#    screen.blit(snake, apple)
    pygame.display.flip()


def grid(display, rows, background):
    position = display // rows
    x, y = 0, 0
    for l in range(rows):
        x += position
        y += position
        pygame.draw.line(background, (0, 0, 0), (x,0),(x,display))
        pygame.draw.line(background, (0, 0, 0), (0,y),(display,y))


def apple(display, background):
    global apple_pos_list, snack
    
    if apple_pos_list[4] == False:
        position = display // rows
        x = random.randrange(0, display, position)
        y = random.randrange(0, display, position)
        a, b = 0, 0
        a += position
        b += position
        apple_pos_list = [x, y, a, b, True] #generated positions are stored in pos_list
    pygame.draw.rect(background, (220, 0, 0), (apple_pos_list[0], apple_pos_list[1], apple_pos_list[2], apple_pos_list[3]))
    return apple_pos_list


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


    # Game feature
    snack = False
    snake_direction = None
    pos_list = []


    # Generate body
    position = display // rows
    x = random.randrange(0, display, position)
    y = random.randrange(0, display, position)
    body = [0, 0]
    body[0] = x
    body[1] = y
    
    
    while True:
        # Initialise frames
#        pygame.time.delay(40)
        clock.tick(10)

        
        
        snake.move(display, snake_direction, body)
        redraw_screen(background)


if __name__ == "__main__": main()
