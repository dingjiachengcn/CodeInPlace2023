import pygame
import time
import random

class Game:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.block_size = 20
        self.game_over = False

        # initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")

        # initialize snake and food
        self.snake = Snake(self.screen, self.block_size)
        self.food = Food(self.screen, self.screen_width, self.screen_height, self.block_size)

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    self.snake.change_direction(event.key)
            self.snake.move()
            self.check_collision()
            self.draw()
            time.sleep(0.3)

        pygame.quit()

    def check_collision(self):
        if self.snake.body[0] == self.food.pos:
            self.snake.eat()
            self.food.randomize_position()
        elif self.snake.body[0] in self.snake.body[1:]:
            self.game_over = True
        elif (self.snake.body[0][0] < 0 or
              self.snake.body[0][0] >= self.screen_width or
              self.snake.body[0][1] < 0 or
              self.snake.body[0][1] >= self.screen_height):
            self.game_over = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw()
        self.food.draw()
        pygame.display.update()

class Snake:
    def __init__(self, screen, block_size):
        self.screen = screen
        self.block_size = block_size
        self.direction = "R"
        self.body = [[100, 50], [80, 50], [60, 50]]

    def change_direction(self, key):
        if key == pygame.K_UP:
            self.direction = "U"
        elif key == pygame.K_DOWN:
            self.direction = "D"
        elif key == pygame.K_LEFT:
            self.direction = "L"
        elif key == pygame.K_RIGHT:
            self.direction = "R"

    def move(self):
        head = list(self.body[0])
        if self.direction == "R":
            head[0] += self.block_size
        elif self.direction == "L":
            head[0] -= self.block_size
        elif self.direction == "U":
            head[1] -= self.block_size
        elif self.direction == "D":
            head[1] += self.block_size
        self.body.insert(0, head)
        self.body.pop()

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(x, y, self.block_size, self.block_size))

    def eat(self):
        self.body.append(self.body[-1])

class Food:
    def __init__(self, screen, screen_width, screen_height, block_size):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.pos = [block_size * random.randint(0, screen_width//block_size - 1),
                    block_size * random.randint(0, screen_height//block_size - 1)]

    def randomize_position(self):
        self.pos = [self.block_size * random.randint(0, self.screen_width//block_size - 1),
                    self.block_size * random.randint(0, self.screen_height//block_size - 1)]

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.pos[0], self.pos[1], self.block_size, self.block_size))

if __name__ == "__main__":
    Game().run()
