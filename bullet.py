import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Class designed to manage bullets.'''

    def __init__(self, ai_game):
        '''Create a missile object at the ship's current position.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creating a bullet rectangle at point (0,0) and then defining the appropriate position for it.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Projectile position is defined by float value.
        self.y = float(self.rect.y)

    def update(self):
        '''Moving the missile on the screen.'''
        # Missile position update.
        self.y -= self.settings.bullet_speed
        # Updating the position of the bullet rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        '''Display of the missile on the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)