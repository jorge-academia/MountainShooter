from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rectangle.centerx -= ENTITY_SPEED[self.name]
        if self.rectangle.right <= 0:
            self.rectangle.left = WIN_WIDTH