import random
from constants import *
class Food:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT

        self.position = [random.randrange(1, (WIDTH//10)) * 10,
                         random.randrange(1, (HEIGHT//10)) * 10]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randrange(1, (WIDTH//10)) * 10,
                             random.randrange(1, (HEIGHT//10)) * 10]
            self.is_food_on_screen = True
        return self.position

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.position[0], self.position[1], 10, 10))

    def set_food_on_screen(self, choice):
        self.is_food_on_screen = choice