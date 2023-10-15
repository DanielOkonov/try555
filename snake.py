from constants import *

class Snake:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.position = [100, 50]
        self.body = [[100, 50],
                     [90, 50],
                     [80, 50]]
        self.direction = 'RIGHT'

    def change_direction(self, new_direction):
        if new_direction == 'RIGHT':
            self.direction = 'RIGHT'
        if new_direction == 'LEFT':
            self.direction = 'LEFT'
        if new_direction == 'UP':
            self.direction = 'UP'
        if new_direction == 'DOWN':
            self.direction = 'DOWN'

    def move(self, food_position):
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10

        self.body.insert(0, list(self.position))

        if self.position == food_position:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        if self.position[0] >= WIDTH or self.position[0] <= 0 or \
           self.position[1] >= HEIGHT or self.position[1] <= 0:
            return True
        for segment in self.body[1:]:
            if segment == self.position:
                return True
        return False

    def get_head_position(self):
        return self.position

    def get_body(self):
        return self.body
