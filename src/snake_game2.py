import pygame, sys, random
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        self.x = random.randint(0, 40 - 1)
        self.y = random.randint(0, 40 - 1)
        self.pos = Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*20,self.pos.y*20,20,20)
        pygame.draw.rect(screen, ('red'), fruit_rect)


pygame.init()
clock = pygame.time.Clock()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
fruit = Fruit()
while True:
    screen.fill((175,215,70))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(144)
