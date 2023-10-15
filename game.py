import pygame
import sys
from snake import Snake
from food import Food
from autopilot import auto_pilot
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.SysFont(None, 55)
        self.width = WIDTH
        self.height = HEIGHT

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + 20:
            if y1 >= y2 and y1 < y2 + 20:
                return True
        return False

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def game_over(self):
        self.screen.fill((0, 0, 0))
        game_over_text = self.font.render(f"Game Over! Your Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.width // 2 - 200, self.height // 2 - 20))
        pygame.display.flip()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            food_position = self.food.position  # Accessing position directly from Food class
            food_eaten = self.snake.move(food_position)

            if food_eaten:
                self.score += 1
                self.food.set_food_on_screen(False)  # Indicate food has been eaten
                self.food.spawn_food()  # Spawn new food

            self.snake.draw(self.screen)  # Draw snake on screen
            self.food.draw(self.screen)  # Draw food on screen
            self.display_score()  # Display the score

            pygame.display.update()  # Update the display

            if self.snake.check_collision():  # Add this block
                self.game_over()

            self.clock.tick(30)

if __name__ == "__main__":
    game_instance = Game()
    game_instance.run_game()
