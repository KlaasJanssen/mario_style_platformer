import pygame, sys
from settings import *
from level import Level
from overworld import Overworld

class Game:
    def __init__(self):
        self.max_level = 0
        self.overworld = Overworld(0, self.max_level, self.create_level)
        self.status = 'overworld'


    def create_level(self, current_level):
        self.level = Level(current_level, self.create_overworld)
        self.status = 'level'

    def create_overworld(self, current_level, max_level):
        if max_level > self.max_level:
            self.max_level = max_level
        self.overworld = Overworld(current_level, self.max_level, self.create_level)
        self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
