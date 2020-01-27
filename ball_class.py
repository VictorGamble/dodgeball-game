#imports and CONSTANTS

 
#imports
import pygame 
import random
# from player_class import *
from os import path
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)


img_dir = path.join(path.dirname(__file__), 'img')
ball_img = pygame.image.load(path.join(img_dir, "sphere-11.png"))

#CONST
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.transform.scale(ball_img, (25,25))

        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        #draw a circle
        self.radius = int(self.rect.width * .85/ 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # center the sprite on the screen
        self.rect.centerx = int(WIDTH / 2.5)
        self.rect.bottom = int(HEIGHT / 2.5)
        self.speedx = -10

    def update(self):
            # any code here will happen every time the game loop updates
        if self.rect.centerx > WIDTH:
            self.kill()
            new_ball()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.rect.x -= self.speedx

def new_ball():
    b = Ball()
    all_balls.add(b)
    all_sprites.add(b)
        
    

        

    




class Player(pygame.sprite.Sprite):
     # sprite for the Player
    def __init__(self):
            # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
            # create a plain rectangle for the sprite image
        self.image = pygame.transform.scale(ball_img, (25,25))

            # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
            #draw a circle
        self.radius = int(self.rect.width * .85/ 2)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            # center the sprite on the screen
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = int(HEIGHT / 2)
    





# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodgeball")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_balls = pygame.sprite.Group()
ball1 = Ball()
# player = Player()
all_balls.add(ball1)
all_sprites.add(ball1)
# all_sprites.add(player)

for i in range(1):
    new_ball()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_ball()
        
    


    # Update
    all_sprites.update()
    # check for collisions
    # hits = pygame.sprite.spritecollide(player, all_balls, True)
    # if hits:
    #     # running = False
    #     print("hits")
        
    

    
    
    # Draw / render

    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()




# #player shooting fuct
# def shoot(self):
#     ball1 = Ball(self.center.centerx)