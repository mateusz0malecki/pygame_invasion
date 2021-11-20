import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    '''Class intended for the management of a spacecraft.'''

    def __init__(self, ai_game):
        '''Spaceship initialization and initial position.'''

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads a spaceship image and retrieves its rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Each new spaceship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # The ship's horizontal position is stored as a float value.
        self.x = float(self.rect.x)

        # Options that indicate the movement of the ship.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Upgrade the ship's position based on the option that indicates its movement.'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''Display the spaceship in its current position.'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Placing the ship in the center of the screen when it comes into contact with an alien.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
