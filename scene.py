# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
from player_class import *
from os import path
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    QUIT,
)


img_dir = path.join(path.dirname(__file__), 'img')
ball_img = pygame.image.load(path.join(img_dir, "sphere-11.png"))

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
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
ball1 = Ball()
all_sprites.add(ball1)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                break
        elif event.type == QUIT:
            running = False
            break

    #Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on keypresses
    player.update(pressed_keys)
        # Fill the background with white
    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    surf = pygame.Surface((50,50))
    surf.fill((255,33,127))
    rect = surf.get_rect()

    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT -surf.get_height())/2
    )

    screen.blit(player.surf, player.rect)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()