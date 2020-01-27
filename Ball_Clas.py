#imports and CONSTANTS

 
#imports
import pygame 
import random
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

keys = pygame.key.get_pressed()
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
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
        
            
    def update(self):
            # any code here will happen every time the game loop updates
        if keys[K_UP]:
                self.rect.move_ip(0, -5)
      


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
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    
    def update(self):

        def update(self, pressed_keys):
            SCREEN_WIDTH = 800
            SCREEN_HEIGHT = 600
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT






        

        






# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodgeball")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
ball1 = Ball()
ball2 = Ball()
player = Player()
all_sprites.add(ball1)
all_sprites.add(player)
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
    


    # Update
    all_sprites.update()

    # pygame.sprite.spritecollide(Player, Ball, True)
    

    
    
    # Draw / render

    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()




# #player shooting fuct
# def shoot(self):
#     ball1 = Ball(self.center.centerx)