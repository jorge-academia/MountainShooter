import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rectangle.top > 0:
            self.rectangle.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rectangle.bottom < WIN_HEIGHT:
            self.rectangle.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rectangle.left > 0:
            self.rectangle.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rectangle.right < WIN_WIDTH:
            self.rectangle.centerx += ENTITY_SPEED[self.name]
        pass
