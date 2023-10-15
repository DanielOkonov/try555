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
        print(f"Initial position: {self.position}")
        print(f"Initial body: {self.body}")

        # Create a new head position based on the current direction
        new_head = list(self.position)
        if self.direction == 'UP':
            new_head[1] -= 10
        if self.direction == 'DOWN':
            new_head[1] += 10
        if self.direction == 'LEFT':
            new_head[0] -= 10
        if self.direction == 'RIGHT':
            new_head[0] += 10

        # Check if the snake has eaten the food
        if new_head == food_position:
            self.body.insert(0, new_head)  # Add new head and keep the tail (snake grows)
            self.position = new_head  # Update the snake's position
            print(f"Updated position: {self.position}")
            print(f"Updated body: {self.body}")
            return True
        else:
            self.body.pop()  # Remove the tail
            self.body.insert(0, new_head)  # Add new head (snake moves but doesn't grow)
            self.position = new_head  # Update the snake's position
            print(f"Updated position: {self.position}")
            print(f"Updated body: {self.body}")
            return False

    def check_collision(self):
        if self.position[0] >= WIDTH or self.position[0] <= 0 or \
           self.position[1] >= HEIGHT or self.position[1] <= 0:
            return True
        for segment in self.body[1:]:
            if segment == self.position:
                return True
        return False
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))

    def get_head_position(self):
        return self.position

    def get_body(self):
        return self.body
