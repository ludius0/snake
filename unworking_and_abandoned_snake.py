from pygame.locals import *
import pygame, math, random

display = 600
rows = 30
d = display
apple_pos_list = [0, 0, 0, 0, False]
snake_pos_list = []
head = []
body = []
snake_direction = None
score = 0
body_lenght = 1
pos_head = []
turns = {}

class cube():
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

class snake():

    def draw_head():
        global head, pos_head
        position = display // rows
        a, b = 0, 0
        a += position
        b += position
        # Draw a head
        pygame.draw.rect(background, (0, 100, 255), (head[0], head[1], a, b))
        pos_head = [head[0], head[1]]

    def draw_body(): ###### Cant figured out how to draw body in turns(maybe something with dictionaries or list with[-x -> slicing]
        global body, head, pos_head, turns
        position = display // rows
        a, b = 0, 0
        a += position
        b += position

        
        x, y = pos_head

        for i in range(body_lenght):
            body.append(x)
            body.append(y)
            if snake_direction == "LEFT":
                x += a
            elif snake_direction == "RIGHT":
                x -= a
            elif snake_direction == "UP":
                y += b
            elif snake_direction == "DOWN":
                y -= b
            pygame.draw.rect(background, (0, 100, 255), (body[-2], body[-1], a, b))
        

    def move(background, head):
        global snake_direction, body
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                snake_direction = "LEFT"
            elif keys[pygame.K_RIGHT]:
                snake_direction = "RIGHT"
            elif keys[pygame.K_UP]:
                snake_direction = "UP"
            elif keys[pygame.K_DOWN]:
                snake_direction = "DOWN"


        position = display // rows
        x, y = 0, 0
        x += position
        y += position
        

        if head[0] < 0:
            head[0] = 0 
        elif head[1] < 0:
            head[1] = 0
        elif head[0] > display:
            head[0] = display
        elif head[1] > display:
            head[1] = display

        body = [head[0], head[1]]
        if snake_direction == "LEFT":
            head[0] = head[0] - x
                
        elif snake_direction == "RIGHT":
            head[0] = head[0] + x
                
        elif snake_direction == "UP":
            head[1] = head[1] - y
                
        elif snake_direction == "DOWN":
            head[1] = head[1] + y


        snake.draw_head()
        

        snake.collision_apple()
                         
        redraw_screen(background)


    def collision_apple():
        global apple_pos_list, head, score, body_lenght
        if apple_pos_list[0] == head[0] and apple_pos_list[1] == head[1]:
            print("You got an apple!")
            apple_pos_list[-1] = False
            apple(background)
            score += 1
            x = apple_pos_list[0]
            y = apple_pos_list[1]
            body_lenght += 1
            pos_head.append(head[0])
            pos_head.append(head[1])
            
            
            
            
    def collision_snake():
        pass



def redraw_screen(background): #redraw everything on the screen: background, grid, snake and apple
    background.fill((60, 150, 100))
    
    grid(background)
    apple(background)
    snake.draw_head()
    snake.draw_body()
    
    screen.blit(background, (0, 0))
    pygame.display.flip()


def grid(background):   # Generate a grip in form of cubes
    position = display // rows
    x, y = 0, 0
    for l in range(rows):
        x += position
        y += position
        pygame.draw.line(background, (0, 0, 0), (x,0),(x,display))
        pygame.draw.line(background, (0, 0, 0), (0,y),(display,y))


def apple(background):  # Generate snack
    global apple_pos_list, snack
    
    if apple_pos_list[-1] == False:
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
    global screen, background, head, snack
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((display, display))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()


    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()


    # Game feature
    pos_list = []

    # Generate body
    position = display // rows
    x = random.randrange(0, display, position)
    y = random.randrange(0, display, position)
    head = [x, y]
    
    
    
    while True:
        # Initialise frames
#        pygame.time.delay(40)
        clock.tick(10)
        
        
        snake.move(background, head)
        redraw_screen(background)


if __name__ == "__main__":
    main()
    print(f"You scored: {score}")
