import pygame, sys, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def drawn_snake(self):
        for block in self.body:
            x_pos = block.x*40
            y_pos = block.y*40
            block_rect = pygame.Rect(x_pos,y_pos,40,40)
            pygame.draw.rect(screen, ('blue'), block_rect)
    
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*40,self.pos.y*40,40,40)
        pygame.draw.rect(screen, ('red'), fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, 20 - 1)
        self.y = random.randint(0, 20 - 1)
        self.pos = Vector2(self.x,self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_eat()
        self.check_lost()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.drawn_snake()

    def check_eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_lost(self):
        if not 0 <= self.snake.body[0].x < 20 or not 0 <= self.snake.body[0].y < 20:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        print('GAME OVER')
        print(f'SCORE: {len(main_game.snake.body)-3}')
        pygame.quit()
        sys.exit()

pygame.init()
clock = pygame.time.Clock()
width = 20*40
height = 20*40
screen = pygame.display.set_mode((width, height))
main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)    
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
                    
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(144)
